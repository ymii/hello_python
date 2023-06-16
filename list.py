# 文字列"car"、"bike"、"boat"を含むリストを定義。
# print関数で標準出力するとリスト要素の全てが表示される
myList = ["car", "bike", "boat"]
print(myList)

# リストは先頭がインデックス[0]から始まる。myListをインデックス順に標準出力
# 出力結果は"car"
print(myList[0])
# 出力結果は"bike"
print(myList[1])
# 出力結果は"boat"
print(myList[2])

# 一つのリストに異なる種類のデータを含めることもできる。
# 以下のmultiListの要素は文字列、整数、実数（浮動小数点数）が含まれる
multiList = ["car", 10, 3.14]
print(multiList)