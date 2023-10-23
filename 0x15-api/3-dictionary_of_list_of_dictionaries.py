#!/usr/bin/python3
""" Gathering data from an API """
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()

    data = []
    for user in users:
        username = user['username']
        userId = user['id']

        todo = requests.get(url + f"todos").json()
        todo = [task for task in todo if task['userId'] == int(userId)]

        tasks = []
        for task in todo:
            temp = {}
            temp['username'] = username
            temp['task'] = task['title']
            temp['completed'] = task['completed']
            tasks.append(temp)

        data.append({userId: tasks})

    with open(f'todo_all_employees.json', 'w') as f:
        f.write(json.dumps(data))
