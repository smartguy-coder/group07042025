import json

our_data = {
    'name': "alex",
    "age": 15,
    'is_healthy': True,
    'more_info': None,
    'hobbies': ['tennis', 'soccer',],
    'ukr': 'мама її помила'
}

# 1 - dict to string
json_string = json.dumps(our_data, ensure_ascii=False)
print(json_string)

# 2 json to dict
dict_from_json = json.loads(json_string)
print(dict_from_json)

# 3 dict to file
# with open('alex.json', mode='w') as file:
#     json.dump(our_data, file)

# with open('alex2.json', mode='w', encoding='utf-8') as file:
#     json.dump(our_data, file, ensure_ascii=False, indent=4)

# 4 file to dict
with open('alex2.json', mode='r', encoding='utf-8') as file:
    content = json.load(file)
    print(content)
