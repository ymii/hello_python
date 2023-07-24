# def文で関数（function）を定義する。greeting関数は呼び出されると"hello python"と出力する
def greeting():
    print("hello python")

# greeting関数の呼び出し
greeting()


# 引数を受け取って計算結果を出力する関数の定義。以下では引数xを受け取って関数内でxに10を足す
def add_num(x):
    y = x + 10
    print(y)

# 関数add_numの呼び出し。括弧内に受け渡す引数を指定する
add_num(5)


# 戻り値を返す関数にはreturn文を持たせる。以下の関数では引数xに20を足した結果を返す
def get_sum(x):
    y = x + 20
    return y

# 関数get_sumを呼び出し、nに関数の戻り値を渡す
n = get_sum(5)
print(n)


# 関数の引数は複数指定することができる。以下の関数では２つの引数x、yを受け取り、計算結果を返す
def get_multiply(x, y):
    z = x * y
    return z

# 関数get_multiplyに２つの引数を指定して呼び出し、pに関数の戻り値を渡す
p = get_multiply(10, 5)
print(p)


# 関数の引数にはデフォルト値を指定することができる。引数なしで呼び出されるとデフォルト値が使用される
def country_function(country = "日本"):
    print(country + "人です")

# 関数country_functionに引数を渡して呼び出す
country_function("英国")
# 関数country_functionに引数を渡さず呼び出す
country_function()


# 関数の引数にはリストや辞書型などのデータ型を渡すことができる。以下の関数はリストを引数として受け取り、for文でリスト要素を出力する
def user_function(u_list):
    for i in u_list:
        print(i)

# リストを生成して関数user_functionに引数として渡す
user_list = ["田中", "鈴木", "上野"]
user_function(user_list)


# 以下の関数では辞書型を引数として受け取り、for文で各要素の値を出力する
def user_dict_function(u_dict):
    for i in u_dict:
        print(u_dict[i])

# 辞書型user_dictを生成して、関数user_dict_functionに引数として渡す
user_dict = {
    "user1" : "佐藤",
    "user2" : "高橋",
    "user3" : "中村"
}
user_dict_function(user_dict)