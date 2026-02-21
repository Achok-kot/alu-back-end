#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, uid)).json()
    todos = requests.get("{}/todos?userId={}".format(url, uid)).json()
    data = {uid: [{"task": t.get("title"), "completed": t.get("completed"),
                   "username": user.get("username")} for t in todos]}
    with open("{}.json".format(uid), "w") as f:
        json.dump(data, f)
