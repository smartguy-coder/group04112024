import json

data = [
    {'number': 13, 'name': 'John', 'surname': 'Коноплянка'},
    {'number': 144, 'name': 'John', 'surname': 'Other'},
]

# 1 dict to json string
new_json_string = json.dumps(data)
new_json_string_unicode = json.dumps(data, ensure_ascii=False)

# 2 json string into dict
revert_data = json.loads(new_json_string)

# 3 create json file
with open('json_data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

# 4 read from json file
with open('json_data.json', mode='r', encoding='utf-8') as file:
    data_from_file = json.load(file)
