#!/usr/bin/python3
""" Python CVS """

import json
import requests

if __name__ == '__main__':
    url_todos = "https://jsonplaceholder.typicode.com/users"
    name_users = requests.get(url_todos, verify=False).json()
    list_tasks = {}
    for user in name_users:
        api_todos = requests.get(url_todos + '/{}/todos'
                                 .format(user['id'])).json()
        list_tasks[user['id']] = [{'task': task.get('title'),
                                   'completed': task.get('completed'),
                                   'username': user['username']}
                                  for task in api_todos]
    with open("todo_all_employees.json", 'w', newline='') as jsonfile:
        json.dump(list_tasks, jsonfile)
