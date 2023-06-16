# 文字列"car"、"bike"、"boat"を含むリストを定義してprint関数で標準出力
myList = ["car", "bike", "boat", "apple"]
print(myList)

# リストの要素を置き換える場合は置き換え要素のインデックスを指定して代入する。
# myListの要素"apple"を"banana"に置き換えるにはappleのインデックス[2]を指定。
# 標準出力の結果は["car", "bike", "banana", "apple"]となる
myList[2] = "banana"
print(myList)

# removeメソッドを使用して特定の要素をリストから除く。
# 以下の出力結果は["car", "bike", "apple"]となる
myList.remove("banana")
print(myList)

# インデックスを指定して要素を取り除くにはpopメソッドを使用する。
# myListから"bike"を取り除くにはインデックス[1]を指定。
# 以下の出力結果は["car", "apple"]となる
myList.pop(1)
print(myList)

# clearメソッドを使用するとリスト要素全てが削除され、空のリストになる。
# print関数で標準出力しても何も表示されない
myList.clear()
print(myList)