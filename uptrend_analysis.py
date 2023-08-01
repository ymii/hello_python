import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import sys
import mysql.connector
from mysql.connector import Error
import usTickersModule as usTickers


# 処理を強制終了させる関数
def exit_sys(msg):
    print("[処理を終了します]: " + msg)
    sys.exit()


# テーブルus_aggregateから対象銘柄のtimestampと終値を抽出してDataFrameに格納。
# 抽出条件はtimestamp降順
def getClosePrice(targetTicker):
    closeData = pd.DataFrame()
    sqlQuery = "select timestamp, close from us_aggregate where ticker = %s order by timestamp desc"
    sqlParams = (targetTicker,)
    dbCursor.execute(sqlQuery, sqlParams)
    result = dbCursor.fetchall()

    if len(result) > 0:
        columnList = ["timestamp", "close"]
        closeData = pd.DataFrame(result, columns=columnList)

    return closeData


# 終値のDataFrameを展開して上昇トレンドの日数をカウントする。
# 対象日の終値が前日より高い場合はuptrendCountを加算する
def getUptrendCount(targetDf, rows):
    i = 0
    uptrendCount = 0
    while i < rows - 1:
        timestampA = targetDf.loc[i, "timestamp"]
        closeA = targetDf.loc[i, "close"]
        timestampB = targetDf.loc[i + 1, "timestamp"]
        closeB = targetDf.loc[i + 1, "close"]

        if closeA > closeB:
            uptrendCount += 1
        else:
            break

        i += 1

    return uptrendCount


# usTickersModuleから米国銘柄一覧をリストとして取得
tickerList = usTickers.getUsTickersList()

# データフレームのカラムとして使用
columnList = [
    "ticker",
    "open",
    "high",
    "low",
    "close",
    "transaction",
    "timestamp",
    "volume",
    "vwavg",
]

# MySQLデータベース接続に必要な情報の入力を求める
print("[MySQL host]:")
mysqlHost = str(input())

print("[MySQL user]:")
mysqlUser = str(input())

print("[MySQL password]:")
mysqlPassword = str(input())

print("[MySQL database]:")
mysqlDatabase = str(input())

# 対象銘柄の指定
print('[ticker] for all tickers, type "all_tickers:"')
ticker = str(input())

# 個別銘柄指定でtickerListに対象銘柄がない場合は処理を中断する
if ticker != "all_tickers":
    if ticker not in tickerList:
        exit_sys("該当する銘柄が見当たりません")

# MySQLデータベースに接続。接続に失敗した場合は処理を終了する
db = None
dbCursor = None
try:
    db = mysql.connector.connect(
        host=mysqlHost, user=mysqlUser, password=mysqlPassword, database=mysqlDatabase
    )
    dbCursor = db.cursor(buffered=True)
except Error as e:
    exit_sys("データベース接続に失敗しました。プロセルを終了します")

# 全銘柄指定の場合はtickerListを展開して各銘柄の終値をgetClosePrice関数から取得する。
# 個別銘柄の場合は対象銘柄の終値をgetClosePrice関数から取得する。
# 取得した終値はtimestampとともに辞書型closeDfに格納される。
# 辞書型closeDfをgetUptrendCount関数に渡して連続上昇日数を求める。
# 上昇日数の結果は辞書型resultDictに格納
resultDict = {}
if ticker == "all_tickers":
    for t in tickerList:
        print("ticker: " + t)
        innerDict = {}
        closeDf = getClosePrice(t)
        rowsCount = closeDf.shape[0]
        if rowsCount == 0:
            innerDict = {"uptrendDays": "", "msg": "data not found"}
        else:
            uptrendDays = getUptrendCount(closeDf, rowsCount)
            innerDict = {"uptrendDays": uptrendDays, "msg": ""}

        resultDict[t] = innerDict
else:
    print("ticker" + ticker)
    closeDf = getClosePrice(ticker)
    rowsCount = closeDf.shape[0]
    if rowsCount == 0:
        innerDict = {"uptrendDays": "", "msg": "data not found"}
    else:
        uptrendDays = getUptrendCount(closeDf, rowsCount)
        innerDict = {"uptrendDays": uptrendDays, "msg": ""}

    resultDict = {ticker: innerDict}

# 辞書型resultDictをJSONファイルとして出力。
# 既存ファイルは上書きされる。ファイル名は"uptrend_日付"となる
d = datetime.now().date()
jsonFileName = "uptrend_" + str(d).replace("-", "") + ".json"
with open(jsonFileName, "w") as jsonFile:
    json.dump(resultDict, jsonFile)
