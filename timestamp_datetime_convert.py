from datetime import datetime


# timestampをdatetimeに変換。引数にtimestampと秒(s)もしくはミリ秒(ms)を指定する。
def getDateTime(timestamp, unitType):
    if unitType == "s":
        return datetime.fromtimestamp(timestamp)
    elif unitType == "ms":
        return datetime.fromtimestamp(timestamp / 1000)
