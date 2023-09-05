import pandas_datareader as pdr
import datetime
import yfinance as yf
import pandas as pd
import json

# floatの表示方法を設定する
pd.set_option("display.float_format", "{:.6f}".format)

# TypeError: string indices must be integersを回避するためにpdr_overrideを実行
yf.pdr_override()

# 抽出期間を指定
print("[開始日 yyyy-mm-dd]")
startDate = input()

print("[終了日 yyyy-mm-dd]")
endDate = input()

# 対象銘柄を指定。証券コードの末尾に東京証券取引所のTをつける
# データフレームのカラムは"Open"、"High"、"Low"、"Close"、"Adj Close"、"Volume"。
# インデックスはDate
print("[銘柄]")
ticker = input()
df = pdr.data.DataReader(ticker, start=startDate, end=endDate)

# 対象期間のデータフレームdfに含まれる"High"の最高値を求める
maxHigh = df["High"].max()

# "High"がmaxHighと一致するすべての列をdfから抽出
maxMatchingRows = df[df["High"] == maxHigh]

# maxMatchingRowsを展開して最高値の日付を抽出してリストに格納
maxHighDateList = []
for row in maxMatchingRows.itertuples():
    maxHighDateList.append(str(row.Index))

# JSON出力
resultDict = {"ticker": ticker, "swingHigh": maxHigh, "date": maxHighDateList}
with open("swing_high_pdr.json", "w") as jsonFile:
    json.dump(resultDict, jsonFile)
