#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, sys.argv[1])).json()
    todos = requests.get("{}/todos?userId={}".format(url, sys.argv[1])).json()
    done = [t for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for t in done:
        print("\t {}".format(t.get("title")))
