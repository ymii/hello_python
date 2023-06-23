import pandas as pd
import json
import urllib.request
from urllib.request import urlopen
import time
import mysql.connector
from mysql.connector import Error
import datetime
import dateutil.relativedelta as rDelta
import math


# CSV形式で取得した楽天証券の取り扱い米国銘柄一覧をデータフレームとして読み込む。
# shapeでデータ件数を求め、データフレームを展開して各銘柄の"現地コード"を抽出。
# 抽出した現地コードは文字列としてリストに追加
def getUsTickersList():
    tList = []
    usTickers = pd.read_csv("rakuten_us_tickers.csv", header=0)
    dfLen = usTickers.shape[0]
    i = 0
    while i < dfLen:
        tList.append(str(usTickers.loc[i, "現地コード"]))
        i += 1
    return tList


# polygon.ioの株価API Aggregatesに接続するURLを生成
# 引数は銘柄、開始日、終了日、APIキー
def getAggregateUrl(ticker, startDate, endDate, apiKey):
    url = (
        "https://api.polygon.io/v2/aggs/ticker/"
        + ticker
        + "/range/1/day/"
        + str(startDate)
        + "/"
        + str(endDate)
        + "?adjusted=true&sort=asc&limit=1000&apiKey="
        + apiKey
    )
    return url


# 各銘柄のus_aggregateの最新日を抽出。timestamp型をdatetime型に変換する。
# 結果をタプルで返し、日足抽出期間のstartDateとして使用する
def getLastDatetime(ticker):
    result = None
    try:
        dbCursor.execute(
            "SELECT MAX(timestamp) FROM us_aggregate WHERE ticker=%s", (ticker,)
        )
        result = dbCursor.fetchone()
    except Error as e:
        errorLogList.append("[" + ticker + "] 最新日の抽出に失敗")

    if result is None or result[0] is None:
        return (False,)

    dt = datetime.date.fromtimestamp(result[0] / 1000.0)
    return (True, dt)


# 基準日からn年前の日付を取得。日足抽出期間のendDateとして使用する。
# まとめて年単位のデータを抽出する際に使用
def getMinusNYear(baseD, n):
    minusNYearDate = baseD - rDelta.relativedelta(years=n)
    return minusNYearDate


# 辞書型の日足からclose(c)、high(h)、low(l)、transaction(n)、
# open(o)、timestamp(t)、volume(v)、volume weighted average(vw)を抽出。
# 抽出結果をus_aggregateのテーブルに追加する。
# queryCount、resultsCount、rowCountTotalをタプルとして返す
def dailyInsert(aggDict):
    ticker = aggDict["ticker"]
    queryCount = aggDict["queryCount"]
    resultsCount = aggDict["resultsCount"]
    status = aggDict["status"]
    rowCountTotal = 0
    if queryCount == resultsCount:
        resultsList = aggDict["results"]
        for r in resultsList:
            close = r["c"]
            high = r["h"]
            low = r["l"]
            transaction = r["n"]
            open = r["o"]
            timestamp = r["t"]
            volume = r["v"]
            vwAvg = r["vw"]

            inQuery = "INSERT INTO us_aggregate (ticker, open, high, low, close, transaction, timestamp, volume, vwavg) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            inValues = (
                ticker,
                open,
                high,
                low,
                close,
                transaction,
                timestamp,
                volume,
                vwAvg,
            )

            try:
                dbCursor.execute(inQuery, inValues)
                db.commit()
                rowCountTotal += dbCursor.rowcount
            except Error as e:
                errorLogList.append("[" + ticker + "] us_aggregateテーブルに追加失敗")

    return (queryCount, resultsCount, rowCountTotal)


# ログの出力
def printLog(log, logName):
    print("-------------------------------------")
    print(logName, " ", len(log), "件")
    for x in log:
        print(x)


# 関数getUsTickersListから米国銘柄のリストを取得
usTickersList = getUsTickersList()

# 抽出期間の最終日は現時刻とする
endDate = datetime.date.today()

# us_aggregateに過去の日足がない場合、抽出期間の開始日は現時刻から1年前とする
nYears = 1
startDateDefault = getMinusNYear(endDate, nYears)

# Polygon.ioのAPIキーを求める。APIキーはpolygonで登録して取得
print("Polygon.ioのAPIキーを入力:")
apiKey = str(input())

# ログ用の日時を設定
logDate = datetime.datetime.now()

# polygon.ioのBasicプランは１分間のAPIリクエストに上限があるため、
# リクエストの間隔を空ける
sleepSec = 20

# MySQLのdb_us_stockに接続してcursorオブジェクトを生成
print("MySQL host:")
mysqlHost = str(input())

print("MySQL user:")
mysqlUser = str(input())

print("MySQL password:")
mysqlPassword = str(input())

print("MySQL database:")
mysqlDatabase = str(input())

# 更新ログを保持するリスト
updateLogList = []

# エラーログを保持するリスト
errorLogList = []

db = None
dbCursor = None
try:
    db = mysql.connector.connect(
        host=mysqlHost, user=mysqlUser, password=mysqlPassword, database=mysqlDatabase
    )
    dbCursor = db.cursor(buffered=True)
except Error as e:
    errorLogList.append("データベース接続に失敗")

# Polygon.ioのBasicプランは１分間のAPIリクエストが５回までのため間隔（sleepSec）を空ける。
# 開始日startDateはgetLastDatetime関数から各銘柄の最新日を求める。過去の日足がない場合は、
# startDateDefaultを開始日とする。
if dbCursor is not None:
    for ticker in usTickersList:
        print("ticker: ", ticker)

        lastUpdate = getLastDatetime(ticker)

        startDate = (
            lastUpdate[1] + datetime.timedelta(days=1)
            if lastUpdate[0] == True
            else startDateDefault
        )

        print("startDate: ", startDate)

        url = getAggregateUrl(ticker, startDate, endDate, apiKey)
        insertResult = None
        try:
            response = urllib.request.urlopen(url)
            aggregateDict = json.loads(response.read())
            insertResult = dailyInsert(aggregateDict)
        except urllib.error.HTTPError as e:
            errorLogList.append("[" + ticker + "] HTTPError " + str(e.code))

        if insertResult is not None:
            if insertResult[0] == insertResult[1] == insertResult[2]:
                updateLogList.append("[" + ticker + "] update success")
            else:
                updateLogList.append("[" + ticker + "] update failed")
        else:
            updateLogList.append("[" + ticker + "] update failed")

        time.sleep(sleepSec)

# 更新ログの出力
if len(updateLogList):
    printLog(updateLogList, "更新ログ")

# エラーログを出力
if len(errorLogList):
    printLog(errorLogList, "エラーログ")
