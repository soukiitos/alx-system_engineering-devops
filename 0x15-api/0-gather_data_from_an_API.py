#!/usr/bin/python3
'''Return information about TODO list progress'''
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    nameurl = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [
            td.get("title") for td in nameurl if td.get("completed") is True
            ]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(nameurl)
        ))
    for c in completed:
        print("\t {}".format(c))
