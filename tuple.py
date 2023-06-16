# タプルの定義。タプルは要素を()で囲み、各要素はカンマで区切る
myTupleA = ("banana", "orange", "grape")
print(myTupleA)

# タプルは重複する要素を含めることができる
myTupleB = ("banana", "orange", "orange", "grape", "mango", "melon")
print(myTupleB)

# タプルには文字列、ブール型、数値などのデータ型を含めることができる
myTupleC = ("banana", 10, True, False)
print(myTupleC)

# 要素が１つだけのタプルを定義する場合は、要素の後ろにカンマが必要
myTupleD = ("apple",)
print(myTupleD)

# タプルに含まれる要素の長さを取得するにはlen()関数を使用する
print(len(myTupleA))
print(len(myTupleB))
print(len(myTupleC))
print(len(myTupleD))

# インデックスを指定してタプルの要素を取得する。インデックスは先頭の0から始まる
print(myTupleA[0])
print(myTupleA[1])
print(myTupleA[2])

# 負の値でインデックスを指定すると、タプルの要素を最後尾から先頭に向かって取得できる。
# 最後尾のインデックスは-1で、myTupleAでは"grape"となる
print(myTupleA[-1])
print(myTupleA[-2])
print(myTupleA[-3])

# 繰返し処理for文を使用して、myTupleAの要素を標準出力
for x in myTupleA:
    print(x)

# 繰返し処理for文を使用して、インデックス順にmyTupleBの要素を標準出力
for x in range(len(myTupleB)):
    print(myTupleB[x])

# インデックスで範囲を指定してタプルの要素を取得する。インデックスの先頭は0から始まる。
print(myTupleB[2:5])

# 取得範囲のインデックスで始まりを省略すると、タプルの先頭から指定要素まで取得する
print(myTupleB[:5])

# 取得範囲のインデックスで終わりを省略すると、タプルの指定要素から最後尾まで取得する
print(myTupleB[2:])