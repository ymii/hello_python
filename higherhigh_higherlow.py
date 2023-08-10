import pandas as pd
from mysql.connector import Error
import sys
import usTickersModule as usTickers
import mysqlDbConnection as dbConnection
import json_write as jsonWrite


# 処理を強制終了させる関数
def exitSys(msg):
    print("[処理を終了します]: " + msg)
    sys.exit()


# 各銘柄の高値（high）をテーブルus_aggregateから抽出。最新日から降順で抽出してSeriesに格納
# 抽出結果が空の場合はNoneを返す
def getHighs(targetTicker):
    query = "select high from us_aggregate where ticker = %s order by timestamp desc"
    queryParam = (targetTicker,)
    dbCursor.execute(query, queryParam)
    result = dbCursor.fetchall()
    if len(result) > 0:
        seriesData = [row[0] for row in result]
        series = pd.Series(seriesData)
        return series
    return None


# 各銘柄の安値（low）をテーブルus_aggregateから抽出。最新日から降順で抽出してSeriesに格納
# 抽出結果が空の場合はNoneを返す
def getLows(targetTicker):
    query = "select low from us_aggregate where ticker = %s order by timestamp desc"
    queryParam = (targetTicker,)
    dbCursor.execute(query, queryParam)
    result = dbCursor.fetchall()
    if len(result) > 0:
        seriesData = [row[0] for row in result]
        series = pd.Series(seriesData)
        return series
    return None


# usTickersModuleから米国銘柄一覧をリストとして取得
tickerList = usTickers.getUsTickersList()

# MySQLデータベース接続に必要な情報の入力を求める
print("[MySQL host]:")
mysqlHost = str(input())

print("[MySQL user]:")
mysqlUser = str(input())

print("[MySQL password]:")
mysqlPw = str(input())

print("[MySQL database]:")
mysqlDb = str(input())

connection, dbCursor = dbConnection.getCursor(mysqlHost, mysqlUser, mysqlPw, mysqlDb)

if connection == None or dbCursor == None:
    exitSys("データベース接続に失敗しました")


# tickerListを展開して各銘柄のhigher highとhigher lowの連続発生日数を求める。
# higher highもしくはhigher lowが途切れた時点で次の銘柄に移行。
# 結果は辞書型resultDictに格納
resultDict = {}
for ticker in tickerList:
    highSeries = getHighs(ticker)
    lowSeries = getLows(ticker)

    if highSeries is None or lowSeries is None:
        continue

    i = 0
    daysCount = 0
    while i < len(highSeries):
        hi1 = highSeries[i]
        hi2 = highSeries[i + 1]
        lo1 = lowSeries[i]
        lo2 = lowSeries[i + 1]

        if hi1 > hi2 and lo1 > lo2:
            daysCount += 1
        else:
            break

        if i == len(highSeries) - 2:
            break

        i += 1
    innerDict = {"daysCount": daysCount}
    resultDict[ticker] = innerDict

# モジュールjson_write.pyに辞書型resultDictを渡してJSON形式で出力。
# 既存ファイルは上書きされる。ファイル名は"higherhigh_higherlow_yyyyMMdd.json"となる
jsonWrite.toJson(True, "higherhigh_higherlow", resultDict)
