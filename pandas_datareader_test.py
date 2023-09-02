import pandas_datareader as pdr
import datetime
import yfinance as yf
import pandas as pd

# floatの表示方法を設定する
pd.set_option("display.float_format", "{:.6f}".format)

# TypeError: string indices must be integersを回避するためにpdr_overrideを実行
yf.pdr_override()

# 抽出期間を指定
startDate = datetime.date(2023, 1, 1)
endDate = datetime.date(2023, 8, 30)

# 対象銘柄を指定。証券コードの後に東京証券取引所のTをつける。
# データフレームのカラムは"Open"、"High"、"Low"、"Close"、"Adj Close"、"Volume"。
# インデックスはDate
ticker = "9984.T"
df = pdr.data.DataReader(ticker, start=startDate, end=endDate)

# head関数で先頭の５行を表示
print(df.head())

# ilocで昇順に"Adj Close"を表示
for i in range(len(df)):
    print(df.iloc[i]["Adj Close"])

# 日経２２５の日足を取得
df = pdr.data.DataReader("^N225", start=startDate, end=endDate)
print(df.head())
