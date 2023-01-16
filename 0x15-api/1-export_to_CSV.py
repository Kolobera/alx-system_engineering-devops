#!/usr/bin/python3
""" Python CVS """

import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}"
    api_todos = requests.get(url_todos.format(user_id), verify=False).json()
    url_names = "https://jsonplaceholder.typicode.com/users/{}"
    name_users = requests.get(url_names.format(user_id), verify=False).json()
    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in api_todos:
            writer.writerow([int(user_id), name_users.get('username'),
                            task.get('completed'), task.get('title')])
