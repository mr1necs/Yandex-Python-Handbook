import json
from sys import stdin

json_file = input()
with open(json_file, encoding="UTF-8") as file_in:
    records = json.load(file_in)

for in_data in stdin:
    name, value = in_data.rstrip("\n").split(" == ")
    records[name] = value

with open(json_file, "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)