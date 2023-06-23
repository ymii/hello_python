import pandas as pd
import math
import mysql.connector
from mysql.connector import Error
import datetime
import time
import dateutil.relativedelta as rDelta

# モジュールusTickersModuleをインポート
import usTickersModule as usTickers


# us_aggregateテーブルから銘柄tkrの対象期間のtimestampと終値を抽出。
# timestampと終値をそれぞれのリストに格納して辞書型にまとめる。
# 抽出結果がない場合はNoneを返す
def getTimeCloseDict(tkr, start, end):
    timestampList = []
    closeList = []
    result = None
    qry = "SELECT timestamp, close FROM us_aggregate WHERE ticker = %s and timestamp > %s and timestamp <= %s order by timestamp asc"

    try:
        dbCursor.execute(qry, (tkr, start, end))
        result = dbCursor.fetchall()
    except Error as e:
        errorMsg = "[" + tkr + "] 対象期間の日足抽出に失敗しました"
        errorLogList.append(errorMsg)

    print(dbCursor.rowcount)
    if dbCursor.rowcount > 0:
        for x in result:
            timestampList.append(x[0])
            closeList.append(x[1])
        timeCloseDict = {"timestamp": timestampList, "closeList": closeList}
        return timeCloseDict

    return None


# 各ログの出力
def logPrinter(log, logName):
    print("-------------------------------------")
    print(logName, " ", len(log), "件")
    for x in log:
        print(x)


print(3 * "\n")

# 単純移動平均の期間（日数）をinputで求める
print("単純移動平均の期間を選択:")
print("[0] 20日")
print("[1] 50日")
smaDaysInput = input()
smaDays = 0
if smaDaysInput == "0":
    smaDays = 20
elif smaDaysInput == "1":
    smaDays = 50

# 抽出期間の終了日となる日時を設定してUnix timestampのミリ秒に変換する
endDate = datetime.datetime.now()
endDateUnix = int(time.mktime(endDate.timetuple()) * 1000)

# 過去データの抽出期間（月数）をinputで求める
print("過去データの抽出期間（月数）を指定: 1 ~ 12:")
spanMonth = int(input())

# endDateから抽出期間の開始日を求めてUnix timestampのミリ秒に変換する
# 抽出クエリでは比較演算子>で期間を選択するため、開始日は-1日で設定する
startDate = (endDate - rDelta.relativedelta(months=spanMonth)) - datetime.timedelta(
    days=1
)
startDateUnix = int(time.mktime(startDate.timetuple()) * 1000)

# モジュールusTickersModuleから米国銘柄を取得してリストに格納
tickerList = usTickers.getUsTickersList()

# 更新ログを保持するリスト
updateLogList = []

# エラーログを保持するリスト
errorLogList = []

# MySQLのdb_us_stockに接続してcursorオブジェクトを生成
print("MySQL host:")
mysqlHost = str(input())

print("MySQL user:")
mysqlUser = str(input())

print("MySQL password:")
mysqlPassword = str(input())

print("MySQL database:")
mysqlDatabase = str(input())

db = None
dbCursor = None

try:
    db = mysql.connector.connect(
        host=mysqlHost, user=mysqlUser, password=mysqlPassword, database=mysqlDatabase
    )
    dbCursor = db.cursor(buffered=True)
except Error as e:
    errorMsg = "データベース接続に失敗しました"
    errorLogList.append(errorMsg)

# 関数getTimeCloseDictから各銘柄の辞書型timeCloseDictを取得する。
# timeCloseDictのcloseListをSeriesに変換して単純移動平均を求める。
# 単純移動平均値のtimestampはtimeCloseDictから取得。
# 結果をsma_us_aggregateテーブルに格納。
# 単純移動平均の値がnanの場合は次に移行する
counter = 0
if len(tickerList) > 0:
    for ticker in tickerList:
        print("[", ticker, "]")
        timeCloseDict = getTimeCloseDict(ticker, startDateUnix, endDateUnix)
        rowCountTotal = 0

        if timeCloseDict is not None:
            closeSeries = pd.Series(timeCloseDict["closeList"])
            rollingResult = closeSeries.rolling(smaDays).mean()
            i = 0
            for r in rollingResult:
                if math.isnan(float(r)):
                    i += 1
                    continue

                inQuery = "INSERT INTO sma_us_aggregate (ticker, timestamp, sma_span, sma) VALUES (%s, %s, %s, %s)"
                inVals = (ticker, timeCloseDict["timestamp"][i], smaDays, r)

                try:
                    dbCursor.execute(inQuery, inVals)
                    db.commit()
                    rowCountTotal += dbCursor.rowcount
                except Error as e:
                    errorMsg = "[" + ticker + "] sma_us_aggregateテーブルへの追加に失敗しました"
                    errorLogList.append(errorMsg)

                i += 1

            updateMsg = "[" + ticker + "] 更新件数 " + str(rowCountTotal)
            updateLogList.append(updateMsg)
        else:
            errorMsg = "[" + ticker + "] 過去の日足データが存在しません"
            errorLogList.append(errorMsg)

        counter += 1
        if counter == 3:
            break
else:
    errorMsg = "tickerList生成に失敗"
    errorLogList.append(errorMsg)

# 更新ログとエラーログを出力
logPrinter(updateLogList, "更新ログ")
logPrinter(errorLogList, "エラーログ")

print(3 * "\n")
