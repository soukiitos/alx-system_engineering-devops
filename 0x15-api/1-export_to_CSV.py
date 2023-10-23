#!/usr/bin/python3
'''Export data in the CSV format'''
import requests
import sys
import csv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    user_name = user.get("user_name")
    nameurl = requests.get(
            url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in nameurl:
            writer.writerow({
                sys.argv[1],
                user_name,
                todo.get("completed"),
                todo.get("title")
                })
