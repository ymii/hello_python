import pandas as pd
from mysql.connector import Error
import sys
import usTickersModule as usTickers
import mysqlDbConnection as dbConnection
import timestamp_datetime_convert as timestampConvert
import json


# 処理を強制終了させる関数
def exitSys(msg):
    print("[処理を終了します]: " + msg)
    sys.exit()


# 指定銘柄を終値を指定日数分抽出。抽出結果はpandasのデータフレームに格納。
# 抽出結果はtimestamp降順のためilocで昇順に変換。抽出結果がからの場合はNoneを返す
def getClose(targetTicker, tradingDays):
    query = "select timestamp, close from us_aggregate where ticker = %s order by timestamp desc limit %s"
    resultDf = pd.read_sql(query, connection, params=(targetTicker, tradingDays))
    if resultDf.shape[0] > 0:
        resultDf = resultDf.iloc[::-1]
        return resultDf
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

# 個別銘柄のコードを求める。銘柄コードがtickersListにない場合は処理を中断する
print("[銘柄]")
ticker = str(input())

# 分析対象期間の入力を求める。単位は取引日数
print("[分析対象期間（取引日数]")
tradingDays = int(input())

# 移動平均を算出する日数の入力を求める
print("[移動平均線の日数]")
windowSize = int(input())

# 移動平均の算出日数が分析対象期間より短い場合は処理を終了
if windowSize > tradingDays:
    exitSys("分析対象期間が短すぎます")

# getClose関数から指定日数分の終値を含むデータフレームを求める。
# pandasのrolling関数で単純移動平均を求めて元のデータフレームに含める。
closeDf = getClose(ticker, tradingDays)
sma = closeDf["close"].rolling(window=windowSize).mean()
closeDf["sma"] = sma
print(closeDf)

connection.close()
