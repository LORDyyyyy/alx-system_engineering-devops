#!/usr/bin/python3
""" Gathering data from an API """
import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f"users/{id}").json()
    todo = requests.get(url + f"todos").json()

    todo = [task for task in todo if task['userId'] == int(id)]
    emp_name = user['username']
    total_tasks = len(todo)
    tasks = [(task['title'], task['completed']) for task in todo]

    data = {id: []}

    for task in tasks:
        temp = {}
        temp['username'] = emp_name
        temp['completed'] = task[1]
        temp['task'] = task[0]

        data[id].append(temp)

    with open(f'{id}.json', 'w') as f:
        f.write(json.dumps(data))
