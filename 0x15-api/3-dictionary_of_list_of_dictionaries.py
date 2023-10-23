#!/usr/bin/python3
'''Export data in the JSON format'''
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()
    all_employee = {}
    for user in users:
        task_l = []
        for t in todos:
            if t.get("userId") == user.get("id"):
                task_data = {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": user.get("username")
                        }
                task_l.append(task_data)
        all_employee[user.get("id")] = task_l
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employee, json_file)
