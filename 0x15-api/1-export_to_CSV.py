#!/usr/bin/python3
""" Gathering data from an API """
import csv
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

    dataset = []

    for task in tasks:
        data = {}
        data['ID'] = int(id)
        data['Name'] = emp_name
        data['Status'] = task[1]
        data['task'] = task[0]

        dataset.append(data)

    with open(f'{id}.csv', 'w') as csvfile:
        fieldnames = dataset[0].keys()

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for row in dataset:
            writer.writerow(row)
