# int()関数を使用して文字列型から整数型に変換。
a = int("10")
# 標準出力の結果は整数10となりtype関数ではintとなる
print(a)
print(type(a))

# int()関数を使用して実数（浮動小数点数）から整数型に変換。
# 変換後は小数点以下が切り捨てられる
b = int(3.14)
# 標準出力の結果は3となるtype関数ではintとなる
print(b)
print(type(b))

# float()関数を使用して文字列を浮動小数点数に変換。
c = float("5")
# 変換後は浮動小数点数5.0となるtype関数ではfloat
print(c)
print(type(c))

# float()関数で文字列型2.8を浮動小数点数に変換。
# 変換後は浮動小数点数2.8となる
d = float("2.8")
print(d)
print(type(d))

# float()関数で整数型を浮動小数点数に変換。
# 整数型７は浮動小数点数7.0となる
e = float(7)
print(e)
print(type(e))

# str()を使用して整数型を文字列型に変換。
# 整数型2をstr()で変換すると文字列型の"2"となる
f = str(2)
print(f)
print(type(f))

# str()を使用して浮動小数点数を文字列に変換
# 浮動小数点数3.14を変換すると文字列型の"3.14"となる
g = str(3.14)
print(g)
print(type(g))
