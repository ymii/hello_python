# for文とrange()関数を使用した繰返し処理。変数aは初期値の0から始まり1ずつ加算される
for a in range(5):
    print(a)

# for文とrange()関数を使用して文字列"python"を５回表示する
language = "python"
for b in range(5):
    print(language)

# for文とrange()関数を使用し、変数cの値が３の場合のみ"I love python"を表示する
for c in range(5):
    print(c)
    if(c == 3):
        print("I love python")

# for文とrange()関数を使用し、文字列を一文字ずつ表示する
userName = "tanaka"
for d in userName:
    print(d)

# 繰返し処理の途中で処理を中断するにはbreakを使用する。ここでは変数eの値が3に達すると処理を中断する
for e in range(5):
    print(e)
    if(e == 3):
        break

# 繰返し処理を中断するbreak文をprint関数の前に記述すると、print関数の実行前に処理が中断される
for f in range(5):
    if(f == 3):
        break
    print(f)

# 繰返し処理をスキップするにはcontinue文を使用する。以下の例ではgが3の場合、ブロック内の処理はスキップされて
# 次の処理に移る
for g in range(5):
    if(g == 3):
        continue
    print(g)

# 繰返し処理の中に別の繰返し処理を行うネスト構造
for h in range(3):
    for i in range(5):
        print(h, " : ", i)