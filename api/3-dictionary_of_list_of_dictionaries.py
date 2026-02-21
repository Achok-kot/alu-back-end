#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    data = {}
    for user in users:
        uid = str(user.get("id"))
        todos = requests.get("{}/todos?userId={}".format(url, uid)).json()
        data[uid] = [{"username": user.get("username"),
                      "task": t.get("title"),
                      "completed": t.get("completed")} for t in todos]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
