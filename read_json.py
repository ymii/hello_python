# pandasをインポート
import pandas as pd

# read_json関数でJSON形式のデータをデータフレームとして読み込む。JSON要素の文字列はダブルクオート"で囲むこと
jsonFruit = '{"a":{"name":"apple", "price":100, "origin":"Japan"}, "b":{"name":"banana", "price":200, "origin":"Taiwan"}}'
dfFruit = pd.read_json(jsonFruit)
print(dfFruit)

# read_json関数の第一引数にファイル名を渡すと、JSON形式のファイルを読み込んでデータフレームに変換される
dfCar = pd.read_json("json_data/samples/car.json")
print(dfCar)
