# pandsをインポート
import pandas as pd

# インデックス指定なしのデータフレーム
pd.set_option("display.max_row", None)
uriageData1 = pd.read_csv("uriage.csv", header=0)

# 行ラベルがないデータフレームからlocで特定の行番号を指定して抽出
print(uriageData1.loc[0])

# 行ラベルがないデータフレームからlocで特定の行番号とカラムを指定して抽出
print(uriageData1.loc[0, "種類"])

# データフレームから全てを抽出
print(uriageData1.loc[:])

# 行番号の範囲を指定して抽出。locの場合、指定範囲の終点までが含まれる
print(uriageData1.loc[0:5])

# 行番号の範囲と特定のカラムを指定して抽出
print(uriageData1.loc[10:15, ["年月", "単価"]])


# インデックス指定ありのデータフレーム
uriageData2 = pd.read_csv("uriage.csv", index_col="年月", header=0)

# 行ラベルが指定されているデータフレームは、行ラベルを指定して抽出する
print(uriageData2.loc["2023-07"])

# 行ラベルの範囲を指定して抽出
print(uriageData2.loc["2024-04":"2024-08"])

# 行ラベルの範囲とカラムの範囲を指定して抽出
print(uriageData2.loc["2024-04":"2024-08", "種類":"個数"])


# 条件式を指定して抽出する。以下の例では売上が5000以上のデータを抽出
print(uriageData1.loc[uriageData1["売上"] > 5000])

# 以下の例では種類がジャガイモのみを抽出
print(uriageData1.loc[uriageData1["種類"] == "ジャガイモ"])

# 複数の条件式を指定して抽出するには"&"もしくは"|"を使用する
# "&"の使用例。種類がジャガイモでなおかつ売上が5000以上を抽出
print(uriageData1.loc[(uriageData1["種類"] == "ジャガイモ") & (uriageData1["売上"] > 5000)])
# "|"の使用例。種類が洗剤もしくは売上が2000未満を抽出
print(uriageData1.loc[(uriageData1["種類"] == "洗剤") | (uriageData1["売上"] < 2000)])

# 条件抽出isinはデータフレーム内に条件と一致する値が存在するデータを抽出する。この例では種類が牛乳もしくはパンの
# データを抽出する
print(uriageData1.loc[uriageData1["種類"].isin(["牛乳", "パン"])])
