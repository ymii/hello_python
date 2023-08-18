import pandas as pd
from mysql.connector import Error
import sys
import usTickersModule as usTickers
import mysqlDbConnection as dbConnection
import json_write as jsonWrite
import timestamp_datetime_convert as timestampConvert
import json


# 処理を強制終了させる関数
def exitSys(msg):
    print("[処理を終了します]: " + msg)
    sys.exit()


# 銘柄のlowをテーブルus_aggregateから抽出。条件の日数分をtimestamp降順で抽出。
# データフレームのカラムはcolumnListを指定する。
# 抽出結果が空の場合はNoneを返す
def getLows(targetTicker, tradingDays):
    query = "select timestamp, low from us_aggregate where ticker = %s order by timestamp desc limit %s"
    queryParams = (targetTicker, tradingDays)
    dbCursor.execute(query, queryParams)
    result = dbCursor.fetchall()
    if len(result) > 0:
        columnList = ["timestamp", "low"]
        df = pd.DataFrame(data=result, columns=columnList)
        return df
    return None


# MySQLデータベース接続に必要な情報の入力を求める
print("[MySQL host]:")
mysqlHost = str(input())

print("[MySQL user]:")
mysqlUser = str(input())

print("[MySQL password]:")
mysqlPassword = str(input())

print("[MySQL database]:")
mysqlDatabase = str(input())

connection, dbCursor = dbConnection.getCursor(
    mysqlHost, mysqlUser, mysqlPassword, mysqlDatabase
)

if connection == None or dbCursor == None:
    exitSys("データベース接続に失敗しました")

# usTickersModuleから米国銘柄一覧をリストとして取得
tickerList = usTickers.getUsTickersList()

# 全銘柄指定もしくは個別銘柄指定を選択。
# 個別銘柄の場合は銘柄コードを求める。銘柄コードがtickerListにない場合は処理を中断する
print("[銘柄]")
ticker = str(input())
if ticker not in tickerList:
    exitSys("指定の銘柄が見当たりません")

# 分析対象期間の入力を求める。単位は取引日数
print("[分析対象期間（取引日数）]")
tradingDays = int(input())

# getLows関数から指定日数分の底値を辞書型lowDFとして取得。lowDFの底値の最小値を含む列を抽出。
# 抽出結果をリストに格納してJSONファイルに出力
lowDF = getLows(ticker, tradingDays)
matchingRows = lowDF[lowDF["low"] == lowDF["low"].min()]
resultList = []
for row in matchingRows.itertuples(index=False):
    rowDateTime = timestampConvert.getDateTime(row.timestamp, "ms")
    rowDict = {"datetime": str(rowDateTime), "swingLow": row.low}
    resultList.append(rowDict)

resultDict = {"ticker": ticker, "swingLows": resultList}
with open("swing_low.json", "w") as jsonFile:
    json.dump(resultDict, jsonFile)
