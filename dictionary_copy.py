# キーと値で辞書型bike_dictを生成
bike_dict = {
    "brand": "honda",
    "year": 2023,
    "price": 1000
}
print(bike_dict)

# copy関数で辞書型bike_dictのコピーを生成する
x_dict = bike_dict.copy()
print(x_dict)

# dict関数で辞書型bike_dictのコピーを生成する
y_dict = dict(bike_dict)
print(y_dict)