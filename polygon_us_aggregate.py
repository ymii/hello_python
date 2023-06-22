import pandas as pd
import json
from urllib.request import urlopen
import time
import mysql.connector
import datetime
import dateutil.relativedelta as rDelta


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


# polygonのAPIキーを返す。APIキーはpolygonで登録して取得
def getPolygonAPIKey():
    return "Ot97nJNCIs7jgHTZLMc2YYU3YlnKdtwq"


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


# us_aggregateの最新日を抽出。timestamp型をdatetime型に変換する。
# 日足抽出期間のstartDateとして使用する
def getLastDatetime(ticker):
    dbCursor.execute(
        "SELECT MAX(timestamp) FROM us_aggregate WHERE ticker=%s", (ticker,)
    )
    result = dbCursor.fetchone()
    print("lastDatetime: ", result[0])
    dt = datetime.datetime.fromtimestamp(result[0] / 1000.0)
    print("dt: ", dt)


# 基準日からn年前の日付を取得。日足抽出期間のendDateとして使用する。
# まとめて年単位のデータを抽出する際に使用
def getMinusNYear(baseD, n):
    minusNYearDate = baseD - rDelta.relativedelta(years=n)
    return minusNYearDate


# 辞書型の日足からclose(c)、high(h)、low(l)、transaction(n)、
# open(o)、timestamp(t)、volume(v)、volume weighted average(vw)を抽出。
# 抽出結果をus_aggregateのテーブルに追加。
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
            dbCursor.execute(inQuery, inValues)
            db.commit()
            rowCountTotal += dbCursor.rowcount

    if rowCountTotal == resultsCount:
        return True

    return False


# ログを更新
def updateLog(log_dt, tkr, upType, isSuccess):
    inQuery = "INSERT INTO us_aggregate_update_log (log_datetime, ticker, update_type, is_success) VALUES (%s, %s, %s, %s)"
    inValues = (log_dt, tkr, upType, isSuccess)
    dbCursor.execute(inQuery, inValues)
    db.commit()


# 関数getUsTickersListから米国銘柄のリストを取得
usTickersList = getUsTickersList()

# 抽出期間の最終日は現時刻とする
endDate = datetime.date.today()

# 抽出期間の開始日は現時刻から1年前とする
nYears = 1
startDate = getMinusNYear(endDate, nYears)

apiKey = getPolygonAPIKey()
logDate = datetime.datetime.now()

# polygon.ioのBasicプランは１分間のAPIリクエストに上限があるため、
# リクエストの間隔を空ける
sleepSec = 20

# MySQLのdb_us_stockに接続してcursorオブジェクトを生成
db = mysql.connector.connect(
    host="localhost", user="root", password="airtime777", database="db_us_stock"
)
dbCursor = db.cursor(buffered=True)

# Polygon.ioのBasicプランは１分間のAPIリクエストが５回までのため、12秒間の間隔を空ける。
for ticker in usTickersList:
    print("ticker: ", ticker)
    url = getAggregateUrl(ticker, startDate, endDate, apiKey)
    response = urlopen(url)
    aggregateDict = json.loads(response.read())
    insertSuccess = dailyInsert(aggregateDict)
    updateLog(logDate, ticker, "insert", insertSuccess)
    time.sleep(sleepSec)
