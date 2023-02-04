#!/usr/bin/python3
""" Python CVS """

import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}"
    api_todos = requests.get(url_todos.format(user_id), verify=False).json()
    url_names = "https://jsonplaceholder.typicode.com/users/{}"
    name_users = requests.get(url_names.format(user_id), verify=False).json()
    list_tasks = {user_id: [{'task': task.get('title'), 'completed':
                  task.get('completed'), 'username': name_users['username']}
                  for task in api_todos]}
    with open("{}.json".format(user_id), 'w', newline='') as jsonfile:
        json.dump(list_tasks, jsonfile)
