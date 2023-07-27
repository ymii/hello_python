import pandas as pd


# 楽天証券で取り扱う米国銘柄の一覧（CSVファイル）をデータフレームとして読み込む。
# shapeでデータ件数を求め、データフレームを展開して各銘柄の"現地コード"を抽出。
# 抽出した現地コードは文字列としてリストに追加して返す
def getUsTickersList():
    tList = []
    usTickers = pd.read_csv("rakuten_us_tickers.csv", header=0)
    dfLen = usTickers.shape[0]
    i = 0
    while i < dfLen:
        tList.append(str(usTickers.loc[i, "現地コード"]))
        i += 1
    return tList
