# キー（key）と値（value）のペアで辞書型を生成
product_dict = {
    "pen": 300,
    "paper": 100,
    "pencil": 200
}

# 辞書型に要素を追加するには[ ]内に新しいキーを設定し、右辺に値を設定する。
# 追加後に全ての要素を出力して"eraser"要素が追加されていることを確認
product_dict["eraser"] = 250
print(product_dict)

# 辞書型の要素数を取得するにはlen関数を使用する
print(len(product_dict))

# 辞書型の値はどんなオブジェクトでも可能。以下の例では文字列の値を持つ要素を追加
product_dict["os"] = "linux"
print(product_dict)

# ブリアン型の値を持つ要素を追加
product_dict["isOpen"] = False
print(product_dict)

# 辞書型の値を変更するにはキーを指定して、右辺に新しい値を設定する
product_dict["isOpen"] = True
print(product_dict)

# 辞書型から要素を削除するにはpop関数を使用する。pop関数の()内に削除対象のキーを指定する
product_dict.pop("isOpen")
print(product_dict)