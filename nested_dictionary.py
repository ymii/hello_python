# ネスト構造された辞書型は要素として辞書型を保持する
student_dict = {
    "student1" : {
        "name" : "山田",
        "age" : 15,
        "gender" : "male"
    },
    "student2" : {
        "name" : "鈴木",
        "age" : 16,
        "gender" : "female"
    },
    "student3" : {
        "name" : "上野",
        "age" : 17,
        "gender" : "male"
    }
}

# len関数で辞書型student_dictの要素数を取得する
print(len(student_dict))

# 辞書型student_dictの各キーをfor文で取得
for k in student_dict:
    print(k)

# 辞書型student_dictの各要素をキーを指定して取得
for k in student_dict:
    print(student_dict[k])

# 辞書型student_dictの各要素の"name"を取得
for k in student_dict:
    print(student_dict[k]["name"])

# ネスト構造の辞書型を生成するには先に要素となる辞書型を作り、最後に他の辞書型に入れることもできる。
# 以下の記述では要素となるteacher1からteacher3を先に作り、最後にteacher_dictに入れる
teacher1 = {
    "name" : "佐藤",
    "age" : 30,
    "gender" : "female"
}

teacher2 = {
    "name" : "高橋",
    "age" : 35,
    "gender" : "male"
}

teacher3 = {
    "name" : "中村",
    "age" : 40,
    "gender" : "female"
}

teacher_dict = {
    "teacher1" : teacher1,
    "teacher2" : teacher2,
    "teacher3" : teacher3
}

print(teacher_dict)