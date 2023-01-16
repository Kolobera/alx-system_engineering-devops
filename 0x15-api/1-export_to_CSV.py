#!/usr/bin/python3
"""A script that gathers data from an API and export it to CSV file."""
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
"""The API's URL."""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            file_name = f"{id}.csv"
            with open(file_name, "w") as file:
                for todo in todos:
                    file.write(f"\"{id}\",\"{user_name}\",\"{todo.get('completed')}\",\"{todo.get('title')}\"\n")
