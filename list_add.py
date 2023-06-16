# "car"、"bike"、"boat"の要素を含むリストを定義してprint関数で標準出力
myList = ["car", "bike", "boat"]
print(myList)

# appendメソッドでリストの最後尾に要素"bicycle"を追加。
# 出力結果は["car", "bike", "boat", "bicycle"]となる
myList.append("bicycle")
print(myList)

# insertメソッドはインデックスを指定して要素を追加できる。
# myList[2]に"apple"を追加。
# 標準出力の結果は["car", "bike", "apple", "boat", "bicycle"]となる
myList.insert(2, "apple")
print(myList)

# extendメソッドを使用すると別のリストを追加できる
# "pen"、"paper"の要素を含むリストyourListを定義してmyListに追加する
# 標準出力の結果は["car", "bike", "apple", "boat", "bicycle", "pen", "paper"]となる
yourList = ["pen", "paper"]
myList.extend(yourList)
print(myList)