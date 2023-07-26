import pandas as pd

# "Category"、"Price"、"Year"からなる辞書型を生成
sales = {
    "Category": ["Jacket", "Shoes", "Boots", "Pants"],
    "Price": [20000, 30000, 22000, 31000],
    "Year": [2018, 2020, 2021, 2020],
}

# 辞書型salesをデータフレームとして読み込む
df = pd.DataFrame(sales)
print(df)

# Categoryで昇順にソートする。昇順ソートがデフォルトのため指定する必要はない
print(df.sort_values(by=["Category"]))

# Categoryで降順にソートする。ascendingをFalseに指定することで降順ソートとなる
print(df.sort_values(by=["Category"], ascending=False))

# Priceで昇順ソートする
print(df.sort_values(by=["Price"]))

# Priceで降順ソートする
print(df.sort_values(by=["Price"], ascending=False))

# 複数のカラムで昇順ソートする。ここではPriceとYearでソートする
print(df.sort_values(by=["Price", "Year"]))

# 複数のカラムで降順ソートする。ここではPriceとYearでソートする
print(df.sort_values(by=["Price", "Year"], ascending=False))
