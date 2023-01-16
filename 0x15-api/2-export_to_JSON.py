#!/usr/bin/python3
"""A script that gathers data from an AP and export it to Json file"""
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            file_name = f"{id}.json"
            with open(file_name, "w") as file:
                file.write("{")
                file.write(f"\"{id}\": ")
                file.write("[")
                lp = []
                for todo in todos:
                    lm="{\"task\": "
                    lm+="\"{}\", \"completed\": {}, \"username\": \"{}\"".format(todo.get('title'), str(todo.get('completed')).lower(), user_name)
                    km=lm+"}"
                    lp.append(km)
                file.write(", ".join(lp))
                file.write("]}")
"""file.write("{\"task\": ")
                    file.write(f"\"{todo.get('title')}\", \"completed\": \"{todo.get('completed')}\", \"username\": \"{user_name}\"")
                    file.write("}, ")"""
