# フレームワークpandasをインポート
import pandas as pd

# 1次元のデータ構造に対応するSeriesを生成
seriesData = pd.Series([10, 7, 2, 20, 9])
print(seriesData)

# Series生成時にインデックスを指定する
seriesDataIndex = pd.Series(
    [10, 7, 2, 20, 9], index=["2019", "2020", "2021", "2022", "2023"]
)
print(seriesDataIndex)

# リストからSeriesを生成するには引数dataにリストの変数を渡す
dataList = [1, 2, 3, 4, 5]
seriesDataList = pd.Series(data=dataList)
print(seriesDataList)

# リストからインデックス指定のSeriesを生成するには引数indexにインデックスのリストを渡す
indexList = ["2019", "2020", "2021", "2022", "2023"]
dataList = [10, 20, 30, 40, 50]
seriesDataList = pd.Series(data=dataList, index=indexList)
print(seriesDataList)

# Seriesには数値型以外にも文字列などのデータ型を格納できる
dataList = ["youtube", "instagram", "tiktok"]
seriesDataList = pd.Series(data=dataList)
print(seriesDataList)
