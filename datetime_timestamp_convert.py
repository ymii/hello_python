from datetime import datetime
from dateutil.relativedelta import relativedelta


# 現在時刻から指定の日数・月数・年数を減算する。
# 引数vは日数：月数・年数、引数periodTypeは日（d）、月（m）、年（y）
def getTimestamp(v, periodType):
    currentDate = datetime.now()
    if periodType == "d":
        x = currentDate - relativedelta(days=v)
        return int(x.timestamp()) * 1000
    elif periodType == "m":
        x = currentDate - relativedelta(months=v)
        return int(x.timestamp()) * 1000
    elif periodType == "y":
        x = currentDate - relativedelta(years=v)
        return int(x.timestamp()) * 1000
