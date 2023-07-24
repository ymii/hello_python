# ライブラリのMySQL Connectorをインポート
import mysql.connector

# host、user、passwordを設定してMySQLに接続。既存のデータベースを選択するにはdatabase="database名"を含める
testDb = mysql.connector.connect(host="localhost", user="username", password="password")

# cursorオブジェクトを準備
testCursor = testDb.cursor(buffered=True)


# データベースを作成
testCursor.execute("CREATE DATABASE testdatabase")

# データベースを表示（全てのデータベースが表示される）
testCursor.execute("SHOW DATABASES")
for x in testCursor:
    print(x)

# USEクエリで作成したデータベースを選択する
testCursor.execute("USE testdatabase")

# 現在選択されているデータベースを確認する
testCursor.execute("SELECT DATABASE()")
print(testCursor.fetchone()[0])


# データベース内にテーブルを作成。
testCursor.execute(
    "CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT)"
)

# データベース内のテーブルを表示
testCursor.execute("SHOW TABLES")
for x in testCursor:
    print(x)

# テーブルの構造を表示
testCursor.execute("DESC product")
for x in testCursor:
    print(x)


# INSERTクエリでテーブルにデータを一件追加する。追加するデータをエスケープ処理するには%sを使用する
query = "INSERT INTO product (name, price) VALUES (%s, %s)"
insertVal = ("牛乳", 150)
testCursor.execute(query, insertVal)
# クエリ実行には接続しているデータベースに対してcommitを指示する
testDb.commit()
# cursorのrowcountで追加されたレコードの件数を取得
print(testCursor.rowcount)
# cursorのlastrowidで最後に追加されたレコードのidを取得
print(testCursor.lastrowid)

# 複数のデータを追加するにはexecutemanyを使用する
query = "INSERT INTO product (name, price) VALUES (%s, %s)"
# 追加するデータをタプリとして準備
insertVal = [("レタス", 100), ("人参", 130), ("ジャガイモ", 200), ("卵", 300), ("りんご", 320)]
testCursor.executemany(query, insertVal)
testDb.commit()
# cursorのrowcountで追加されたレコードの件数を取得
print(testCursor.rowcount)


# SELECTクエリでレコードを抽出。抽出したレコード全てを取得するにはfetchallを使用する
testCursor.execute("SELECT * FROM product")
result = testCursor.fetchall()
for x in result:
    print(x)

# SELECTクエリに抽出するカラムを指定する。
testCursor.execute("SELECT name FROM product")
result = testCursor.fetchall()
for x in result:
    print(x)

# SELECTクエリで抽出したレコードの先頭の一件のみを取得するにはfetchoneを使用する
testCursor.execute("SELECT name FROM product")
result = testCursor.fetchone()
print(result)

# SELECTクエリにWHERE条件を指定してfetchallで全てを取得する
testCursor.execute("SELECT * FROM product where price > 200")
result = testCursor.fetchall()
for x in result:
    print(x)


# UPDATEクエリでレコードを更新する
updateQuery = "UPDATE product SET price = %s WHERE name = %s"
updateVal = (500, "りんご")
testCursor.execute(updateQuery, updateVal)
testDb.commit()

# DELETEクエリでレコードを削除する
deleteQuery = "DELETE FROM product WHERE name = %s"
# 要素が１つだけのタプルは要素の後ろにカンマが必要
deleteVal = ("人参",)
testCursor.execute(deleteQuery, deleteVal)
testDb.commit()


# cursorとデータベース接続を閉じる
testCursor.close()
testDb.close()
