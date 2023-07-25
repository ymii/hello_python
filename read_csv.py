# フレームワークpandasをインポート
import pandas as pd

# Pandasのread_csv関数を使用してcsvファイルをデータフレームとして読み込む。第一引数にファイルパスを指定する。
# csvファイルの先頭行（0行目）はヘッダーのため第二引数にヘッダー行を指定する。サンプルのcsvファイルはgithubから
# ダウンロード。
wine_data1 = pd.read_csv("wine_data.csv", header=0)

# wine_dataをshapeアトリビュートで読み込んだデータの行数と列数を取得
# 取得結果は（行数, 列数）となる
print(wine_data1.shape)

# 読み込んだcsvファイルをhead関数で先頭５行を標準出力
print(wine_data1.head())

# 読み込んだcsvファイルをtail関数で後尾５行を標準出力
print(wine_data1.tail())

# csvファイルを読み込む際、元からあるインデックスを使用するには引数index_colにインデックス名を渡す。
# set_option関数に引数"display.max_rows"と"None"を渡すと全件数を表示できる
pd.set_option("display.max_rows", None)
wine_data2 = pd.read_csv("wine_data.csv", index_col="ID", header=0)
print(wine_data2)
# 読み込んだcsvファイルの先頭５行を表示
print(wine_data2.head())
# 読み込んだcsvファイルの後尾５行を表示
print(wine_data2.tail())
