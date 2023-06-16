# while文で条件式i<5が真の間、ブロック内の処理を続ける
i = 0
while i < 5:
    print(i)
    i += 1

# while文でリスト要素をインデックス順に表示。while条件式の右辺はリストのサイズ（要素数）となる
i = 0
userList = ["田中", "谷口", "吉野", "川中", "鈴木"]
while i < len(userList):
    print(userList[i])
    i += 1

# break文をwhile構造内で使用すると繰り返し処理を中断する。
# 下記の例ではuserListの要素値が"吉野"と一致した場合、処理を中断する
i = 0
while i < len(userList):
    print(userList[i])
    if(userList[i] == "吉野"):
        break
    i += 1

# continue文をwhile構造内で使用すると繰り返し処理をスキップする。
# 下記の例ではuserListの要素値が"谷口"と一致した場合、print(user)の処理がスキップされて次のループに移行する
i = 0
while i < len(userList):
    user = userList[i]
    i += 1
    if(user == "谷口"):
        continue
    print(user)