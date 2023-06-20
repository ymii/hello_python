# pandasをインポート
import pandas as pd

# 1次元のデータ構造に対応するSeriesを生成
pdSeries = pd.Series([10, 25, 53, 14, 5, 26, 87, 48, 9, 16])
print(pdSeries)

# rolling型オブジェクトを表示。rollingの引数に幅を渡す
print(pdSeries.rolling(3))

# 先頭から順に３つずつの要素をもとに合計を求めるにはsumメソッドを呼ぶ
print(pdSeries.rolling(3).sum())

# 先頭から順に３つずつの要素をもとに平均を求めるにはmeanメソッドを呼ぶ
print(pdSeries.rolling(3).mean())

# 先頭から順に３つずつの要素をもとに中央値を求めるにはmedianメソッドを呼ぶ
print(pdSeries.rolling(3).median())

# 先頭から順に３つずつに要素をもとに最大値を求めるにはmaxメソッドを呼ぶ
print(pdSeries.rolling(3).max())

# 先頭から順に３つずつに要素をもとに最小値を求めるにはminメソッドを呼ぶ
print(pdSeries.rolling(3).min())

# 先頭から順に３つずつに要素をもとに標準偏差を求めるにはstdメソッドを呼ぶ
print(pdSeries.rolling(3).std())
