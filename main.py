from pprint import pprint
import requests

URL = 'https://dummyjson.com/todos'
params = {
    'limit': 450,
    'skip': 0
}

response = requests.get(url=URL, params=params)


response_json = response.json()
# pprint(response_json)
todos = response_json['todos']
# pprint(todos)

uncompleted_todos = 0

film_related_todos = []
film_key_word = 'attend'

for todo in todos:
    # todo  {'id': 253, 'todo': 'Try a new fitness class like aerial yoga or barre', 'completed': True, 'userId': 21}
    # print(todo)
    if not todo['completed']:
        uncompleted_todos += 1

    if film_key_word.lower() in todo['todo'].lower():
        film_related_todos.append(todo['todo'])

print(f'{uncompleted_todos=}')
print(f'{film_related_todos=}')


