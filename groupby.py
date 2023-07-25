import pandas as pd

# csvファイルをデータフレームとして読み込む。先頭行をインデックスとして指定する
wine_review = pd.read_csv("./wine_data_2.csv", index_col=0)

# 最初と最後の５行を出力してデータフレームを確認
print(wine_review)

# groupby関数でポイントをグループ化して、count関数で各ポイントの件数を求める
print(wine_review.groupby("points").points.count())

# groupby関数で生産国をグループ化して、count関数で各生産国の件数を求める
print(wine_review.groupby("country").country.count())

# groupby関数で価格をグループ化して、max関数で各グループの最も高いポイントを求める
print(wine_review.groupby("price").points.max())

# groupby関数で生産国をグループ化して、各生産国の最大と最小の価格を求める
print(wine_review.groupby("country").price.agg([min, max]))
