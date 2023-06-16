# ５つの要素を含むリストfruitListを定義
fruitList = ["apple", "grape", "banana", "mango", "orange"]


# 繰り返し処理のforを使用してfruitListの各要素を標準出力する
for x in fruitList:
    print(x)

# 繰り返し処理のforを使用してfruitListの各要素を標準出力し、指定要素"mango"が出力されれば
# break文により繰り返し処理を強制終了する
for x in fruitList:
    print(x)
    if(x == "mango"):
        break


# リストのインデックス順に各要素を標準出力するにはrange関数をlen関数を使用する。
for i in range(len(fruitList)):
    print(fruitList[i])

# リストのインデックス順に各要素を標準出力し、指定要素"banana"が出力されれば
# break文により繰り返し処理を強制終了する
for i in range(len(fruitList)):
    print(fruitList[i])
    if(fruitList[i] == "banana"):
        break