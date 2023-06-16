# 辞書型dictionaryはキー（key）と値（value）のペアで生成し、キーと値はカンマで区切る
product_dict = {
    "pen": 300,
    "paper": 100,
    "pencil": 200
}

# product_dictに含まれる全ての要素を出力
print(product_dict)

# 辞書型の要素にアクセスするには[ ]内にキーを指定する。これによって指定したキーの値を取得する
print(product_dict["pen"])
print(product_dict["paper"])
print(product_dict["pencil"])

# 辞書型の要素にアクセスするにはget関数を使用することもできる
print(product_dict.get("pen"))
print(product_dict.get("paper"))
print(product_dict.get("pencil"))

# 辞書型の要素すべてのキーを取得するにはkeys関数を使用し、取得したキーはリストに格納される。
key_list = product_dict.keys()
print(key_list)

# for文を使用すると辞書型の要素すべてのキーを１つずつ取得できる
for i in product_dict:
    print(i)

# for文で辞書型の要素すべての値を１つずつ取得する
for i in product_dict:
    print(product_dict[i])

# items関数を使用するとキーと値の両方を取得できる
for k, v in product_dict.items():
    print(k, v)