# 条件が真の場合はTrueを返す。
# 以下の条件式5 > 1は真であるためTrueとなる
print(5 > 1)

# 以下の条件式7 == 7は真であるためTrueとなる
print(7 == 7)

# 条件が偽の場合はFalseを返す
# 以下の条件式10 > 5は偽であるためFalseとなる
print(10 < 5)

# 以下の条件式8 == 10は偽であるためFalseとなる
print(8 == 10)

# bool型変数の定義は文字列型や数値型などの変数定義と同様に行う
boolA = True
boolB = False
boolC = False

# 変数boolA、boolB、boolCを標準出力するとそれぞれの真偽値が出力される
print(boolA)
print(boolB)
print(boolC)

# if条件式でbool型を使用する。以下の例ではboolAの値がTrueの場合のみ挨拶が出力される
if boolA == True:
    print("おはよう")
else:
    print("...")

# if条件式の記述は以下のように"== True"を省くことができる
if boolA:
    print("おはよう")
else:
    print("...")

# boolAとboolBを論理演算子のandで比較すると条件式の結果はFalseとなるため、挨拶は表示されない
if boolA and boolB:
    print("こんにちは")
else:
    print("...")

# boolBとboolCを論理演算子のandで比較すると条件式の結果はTrueとなるため、挨拶が表示される
if boolB == False and boolC == False:
    print("こんばんは")
else:
    print("...")