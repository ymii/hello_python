# 文字列変数aを定義して値を代入
a = "Hello, World"
print(a)

# upper()メソッドを使用して変数aの文字列をすべて大文字に変換。
# 変換結果を変数a_upperに代入
a_upper = a.upper()
print(a_upper)

# lower()メソッドを使用して変数aの文字列をすべて小文字に変換。
# 変換結果を変数a_lowerに代入
a_lower = a.lower()
print(a_lower)

# strip()メソッドを使用して文字列の前後に含まれる空白を除去。
b = " I love python "
b = b.strip()
print(b)

# replace()メソッドを使用して文字列に含まれる文字を置き換える。
# 以下では変数bに含まれる"p"を"c"に置き換える
c = b.replace("p", "c")
# 置き換え後は"cython"となる
print(c)

# split()メソッドを使用して特定の区切り文字で文字列を分割。
# 分割された文字列の要素はリストに格納される。
# 以下では変数aの文字列を区切り文字","で分割する。
d = a.split(",")
# 標準出力の結果は['Hello', 'World']
print(d)

# 文字列を結合するには+演算子を使用する。
# 以下では変数aとbを結合し、間に半角空白をいれる
e = a + " " + b
print(e)