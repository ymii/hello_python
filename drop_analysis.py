import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import sys
import mysql.connector
from mysql.connector import Error
import usTickersModule as usTickers


# 処理を強制終了させる関数
def exitSys(msg):
    print("[処理を終了します]: " + msg)
    sys.exit()


# closeAが最新日の終値、closeBがcloseAの前日の終値。
# closeAがcloseBより低い場合のみ下落率を求める
def getDropPercentage(targetDf):
    closeA = targetDf.loc[0, "close"]
    closeB = targetDf.loc[1, "close"]
    dropPercentage = None
    if closeA < closeB:
        dropPercentage = abs(closeB / closeA - 1)

    return dropPercentage


# テーブルus_aggregateから対象銘柄のtimestampと終値を抽出してDateFrameに格納。
# 抽出条件はtimestamp降順で最新日とその前日のみ
def getClosePrice(targetTicker):
    closeData = pd.DataFrame()
    sqlQuery = "select timestamp, close from us_aggregate where ticker = %s order by timestamp desc limit 2"
    sqlParams = (targetTicker,)
    dbCursor.execute(sqlQuery, sqlParams)
    result = dbCursor.fetchall()

    if len(result) > 0:
        columnList = ["timestamp", "close"]
        closeData = pd.DataFrame(result, columns=columnList)

    return closeData


# usTickersModuleから米国銘柄一覧をリストとして取得
tickerList = usTickers.getUsTickersList()

# usTickersModuleから米国銘柄一覧をリストして取得
tickerList = usTickers.getUsTickersList()

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
        exitSys("該当する銘柄が見当たりません")

# MySQLデータベースに接続。接続に失敗した場合は処理を終了する
db = None
dbCursor = None
try:
    db = mysql.connector.connect(
        host=mysqlHost, user=mysqlUser, password=mysqlPassword, database=mysqlDatabase
    )
    dbCursor = db.cursor(buffered=True)
except Error as e:
    exitSys("データベース接続に失敗しました。プロセスを終了します")

# 全銘柄指定の場合はtickerListを展開してgetClosePrice関数から各銘柄の終値を取得。
# 個別銘柄指定の場合は対象銘柄の終値をgetClosePrice関数から取得。
# 取得した終値はtimestampとともに辞書型closeDfに格納される。
# 辞書型closeDfをgetDropPercentage関数に渡して下落率を求める。
# DropPercentage関数の戻り値がNoneの場合は下落が発生しなかったことになる。
# 下落率の結果は辞書型resultDictに格納
resultDict = {}
if ticker == "all_tickers":
    for t in tickerList:
        print("ticker: " + t)
        innerDict = {}
        closeDf = getClosePrice(t)
        rowCount = closeDf.shape[0]
        if rowCount == 2:
            dropPercentage = getDropPercentage(closeDf)
            if dropPercentage != None:
                innerDict = {
                    "dropPercentage": format(dropPercentage * 100, ".2f"),
                    "msg": "",
                }
            else:
                innerDict = {
                    "dropPercentage": "",
                    "msg": "drop in close price not detected",
                }
        else:
            innerDict = {"dropPercentage": "", "msg": "data not found"}

        resultDict[t] = innerDict
else:
    print("ticker: " + ticker)
    closeDf = getClosePrice(ticker)
    rowCount = closeDf.shape[0]
    innerDict = {}
    if rowCount == 2:
        dropPercentage = getDropPercentage(closeDf)
        if dropPercentage != None:
            innerDict = {
                "dropPercentage": format(dropPercentage * 100, ".2f"),
                "msg": "",
            }
        else:
            innerDict = {
                "dropPercentage": "",
                "msg": "drop in close price not detected",
            }
    else:
        innerDict = {"dropPercentage": "", "msg": "data not found"}

    resultDict[ticker] = innerDict

# 辞書型resultDictをJSONフィアルとして出力。
# 既存ファイルは上書きされる。ファイル名は"drop_yyyyMMdd"となる
d = datetime.now().date()
jsonFileName = "drop_" + str(d).replace("-", "") + ".json"
with open(jsonFileName, "w") as jsonFile:
    json.dump(resultDict, jsonFile)
