import json
from diarybook import Diary


def read_from_json_into_app(path):
    with open(path) as file:
        data = json.loads(file.read())
        diaries = []
        for entry in data:
            diaries.append(Diary(entry["user"], entry["memo"], entry["tags"]))
        return diaries


def write_into_json_from_app(user, memo, tags, path):
    with open("data.json", "r") as file:
        data = json.load(file)

    data.append({"user": user, "memo": memo, "tags": tags})

    with open(path, "w") as file:
        json.dump(data, file, indent=5)
