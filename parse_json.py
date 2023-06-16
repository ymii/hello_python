# 標準ライブラリのjsonをインポート
import json

# JSON形式のデータを生成
appleJson = '{"name":"apple", "price":100, "origin":"Japan"}'

# JSON形式のデータを辞書型に読み込む
appleDict = json.loads(appleJson)
# 辞書型の要素を全て表示
print(appleDict)
# 辞書型のキーを指定して表示
print(appleDict["name"])


# 辞書型からJSON形式に変換するにはdumpsを使用する
grapeJson = {"name": "grape", "price": 300, "origin": "Taiwan"}
grapeDict = json.dumps(grapeJson)
# 変換後のJSONを表示
print(grapeJson)


# bool型、リスト、タプル、Noneを含む辞書型をdumpsでJSON形式に変換する。
# リストとタプルはJSON配列に変換される。
# dumpsに引数indentを渡すと変換後のJSONがフォーマットされる
guestDict = {
    "name": "Mike Harris",
    "age": 30,
    "alcohol": True,
    "dislikes": ("onion", "fish"),
    "orders": [{"appetizer": "", "serving": 1}, {"drink": "beer", "serving": 2}],
    "reservation": None,
}
guestJson = json.dumps(guestDict, indent=4)
print(guestJson)
