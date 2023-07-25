# pandasをインポート
import pandas as pd

# read_csv関数でcsvファイルをデータフレームとして読み込む。引数index_colに元からあるインデックス"ID"を渡し、
# 引数headerに先頭の0行目を渡す。また、set_option関数に全件表示を指定する。
# サンプルのcsvファイルはgithubからダウンロード
pd.set_option("display.max_row", None)
wine_data = pd.read_csv("wine_data.csv", index_col="ID", header=0)

# データフレームから特定のカラムをSeriesとして抽出するにはデータフレーム名.カラム名で求める。
countries1 = wine_data.country
print(countries1)

# データフレームから特定のカラムをSeriesとして抽出するにはデータフレーム名["カラム名"]で求めることもできる
countries2 = wine_data["country"]
print(countries2)

# データフレームから特定のカラムをインデックス指定で一件抽出するにはデータフレーム名["カラム名"][インデックス]で求める
country = wine_data["country"][10]
print(country)
