import pandas as pd


# 最大値と最小値の差を求める関数
def min_max_func(x):
    return max(x) - min(x)


# csvファイルをデータフレームとして読み込む。先頭行をインデックスとして指定する
wine_review = pd.read_csv("./wine_data_2.csv", index_col=0)

# 最初と最後の５行を出力してデータフレームを確認
print(wine_review)

# groupbyメソッドでポイントをグループ化して、countメソッドで各ポイントの件数を求める
print(wine_review.groupby("points").points.count())

# groupbyメソッドで生産国をグループ化して、countメソッドで各生産国の件数を求める
print(wine_review.groupby("country").country.count())

# groupbyメソッドで価格をグループ化して、maxメソッドで各グループの最も高いポイントを求める
print(wine_review.groupby("price").points.max())

# groupbyメソッドで価格をグループ化して、maxメソッドで各グループの最も低いポイントを求める
print(wine_review.groupby("price").points.min())

# groupbyメソッドで価格をグループ化して、meanメソッドで各グループの平均ポイントを求める
print(wine_review.groupby("price").points.mean())

# groupbyメソッドで生産国をグループ化して、aggメソッドに複数の関数を同時に実行する
# ここでは各生産国の最大と最小の価格を求める
print(wine_review.groupby("country").price.agg([min, max]))

# groupbyメソッドで生産国をグループ化して、aggメソッドで独自関数を実行する。
# ここではmin_max_funcを実行
print(wine_review.groupby("country").price.agg(min_max_func))
