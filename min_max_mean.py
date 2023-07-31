import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import sys
import json
from dateutil.relativedelta import relativedelta

# モジュールusTickersModuleをインポート
import usTickersModule as usTickers


# アプリケーションを終了させる関数
def exit_sys(msg):
    print("[アプリケーションを終了します]: " + msg)
    sys.exit()


# 引数vは月数もしくは年数。引数periodTypeは月（m）もしくは年（y）。
# 現在時刻から指定の日数・月数・年数を求める
def getStartDate(v, periodType):
    currentDate = datetime.now()
    if periodType == "m":
        x = currentDate - relativedelta(months=v)
        return int(x.timestamp()) * 1000
    elif periodType == "y":
        x = currentDate - relativedelta(years=v)
        return int(x.timestamp()) * 1000


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

print("[ticker]:")
ticker = str(input())

# tickerListに対象tickerがない場合は処理を終了する
if ticker not in tickerList:
    exit_sys("該当する銘柄が見当たりません")

# 対象期間の選択
print("[対象期間の単位 days, months, years]:")
periodType = str(input())

periodStart = None

if periodType == "days":
    print("[対象日数を入力]:")
    inputDays = input()
elif periodType == "months":
    print("[対象月数を入力]:")
    inputMonths = input()
    periodStart = getStartDate(int(inputMonths), "m")
elif periodType == "years":
    print("[対象年数を入力]:")
    inputYears = input()
    periodStart = getStartDate(int(inputYears), "y")
else:
    exit_sys("対象期間の単位が不明です")

db = None
dbCursor = None

# MySQLデータベースに接続。接続に失敗した場合は処理を終了する
try:
    db = mysql.connector.connect(
        host=mysqlHost, user=mysqlUser, password=mysqlPassword, database=mysqlDatabase
    )
    dbCursor = db.cursor(buffered=True)
except Error as e:
    exit_sys("データベース接続に失敗しました。プロセスを終了します")


# テーブルus_aggregateから対象銘柄の指標を抽出。periodTypeが"days"、"months"もしくは"years"で抽出期間の条件が異なる
if periodType == "days":
    sqlQuery = "select ticker, open, high, low, close, transaction, timestamp, volume, vwavg from us_aggregate where ticker = %s order by timestamp desc limit %s"
    queryParams = (ticker, int(inputDays))
elif periodType == "months" or periodType == "years":
    sqlQuery = "select ticker, open, high, low, close, transaction, timestamp, volume, vwavg from us_aggregate where ticker = %s and timestamp >= %s order by timestamp asc"
    queryParams = (ticker, periodStart)

dbCursor.execute(sqlQuery, queryParams)
result = dbCursor.fetchall()

if len(result) == 0:
    exit_sys("対象銘柄の指標が見つかりません")

# 抽出結果をデータフレームとして読み込む。columnListをカラムとして指定。
# 抽出期間の開始日と終了日、終値の最高値、最安値、平均値を取得。
# 取得した情報を辞書型に格納
df = pd.DataFrame(data=result, columns=columnList)
startDatetime = pd.to_datetime(df["timestamp"].min(), unit="ms")
endDatetime = pd.to_datetime(df["timestamp"].max(), unit="ms")
closeMax = df["close"].max()
closeMin = df["close"].min()
closeMean = "%.2f" % df["close"].mean()
volumeMax = df["volume"].max()
volumeMin = df["volume"].min()
volumeMean = "%.2f" % df["volume"].mean()

dict = {
    "ticker": ticker,
    "startDatetime": str(startDatetime),
    "endDatetime": str(endDatetime),
    "days": len(result),
    "closeMax": closeMax,
    "closeMin": closeMin,
    "closeMean": closeMean,
    "volumeMax": volumeMax,
    "volumeMin": volumeMin,
    "volumeMean": volumeMean,
}

# 辞書型に格納された対象銘柄の情報をJSONファイルとして出力。
# 既存ファイルは上書きされる。ファイル名には対象銘柄が先頭に付く
fileName = ticker + "_data.json"
with open(fileName, "w") as jsonFile:
    json.dump(dict, jsonFile)
