# 比較演算子を用いたif条件式。条件式が真Trueの場合ブロック内の処理が実行される
a = 10
b = 1
if a > b:
    print("aはbより大きい")

# 条件式が偽Falseの場合はブロック内の処理が実行されない
c = 10
d = 20
if c > d:
    print("cはdより大きい")

# if...elseは条件式が真の時の処理と偽の時の処理をあわせて記述できる
age = 17
if age > 20:
    print("成人です")
else:
    print("未成年です")

# if条件式の中にif...else処理を持たせるネスト構造の記述
x = 10
if x > 5:
    if x > 15:
        print("xの値は15以上です")
    else:
        print("xの値は15未満です")

# 複数の条件分岐を記述するにはif...elif...elseを使用する。
# 条件式の評価は上から順に行われ、すべての条件式が偽の場合はelse文の処理が実行される
age = 20
if age >= 15 and age <= 34:
    print("若年層です")
elif age >= 35 and age <= 64:
    print("中年層です")
else:
    print("高齢層です")

