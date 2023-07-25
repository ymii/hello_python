# フレームワークpandasをインポート
import pandas as pd

# 整数値型のデータを格納するDataFrame
dataFrame = pd.DataFrame({"Like": [100, 15], "Dislike": [20, 8]})
print(dataFrame)

# 文字列型のデータを格納するDataFrame
dataFrame = pd.DataFrame({"male": ["楽しかった", "つまらなかった"], "female": ["感動した", "退屈した"]})
print(dataFrame)

# indexを指定してdataFrameの各行に行名をつける
dataFrame = pd.DataFrame(
    {"male": ["楽しかった", "つまらなかった"], "female": ["感動した", "退屈した"]}, index=["動画１", "動画２"]
)
print(dataFrame)

# リストからDataFrameを生成するには引数dataにリストを渡す
list = [10, 22, 17, 5, 18]
dataFrame = pd.DataFrame(data=list)
print(dataFrame)

# リストから列名をつけてDataFrameを生成する
list = [2, 9, 1, 4, 6]
dataFrame = pd.DataFrame({"利用者": list})
print(dataFrame)

# リストからインデックスを指定してDataFrameを生成するには引数indexにリストを渡す
indexList = ["2019", "2020", "2021", "2022", "2023"]
salesQtyA = [5, 1, 2, 9, 7]
salesQtyB = [10, 2, 8, 3, 11]
dataFrame = pd.DataFrame({"商品A": salesQtyA, "商品B": salesQtyB}, index=indexList)
print(dataFrame)

# インデックス、列名をリストから指定してDataFrameを生成する
indexList = ["商品A", "商品B", "商品C"]
columnList = ["2019", "2020", "2021", "2022", "2023"]
dataList = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 300, 400, 500]]
dataFrame = pd.DataFrame(data=dataList, index=indexList, columns=columnList)
print(dataFrame)
