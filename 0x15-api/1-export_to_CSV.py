#!/usr/bin/python3
'''Export data in the CSV format'''
import requests
import sys
import csv


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    nameurl = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in nameurl:
            writer.writerow([
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
                ])
