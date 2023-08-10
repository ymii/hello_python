import json
from datetime import datetime


# pandasの辞書型をJSONファイルに出力する。appendDateがTrueの場合は
# ファイル名の先頭にyyyyMMddが付く。
def toJson(appendDate, filename, dict):
    if appendDate:
        d = datetime.now().date()
        jsonFileName = filename + "_" + str(d).replace("-", "") + ".json"
        with open(jsonFileName, "w") as jsonFile:
            json.dump(dict, jsonFile)
    else:
        jsonFileName = filename + ".json"
        with open(jsonFileName, "w") as jsonFile:
            json.dump(dict, jsonFile)
