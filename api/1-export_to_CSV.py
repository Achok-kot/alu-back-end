#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, uid)).json()
    todos = requests.get("{}/todos?userId={}".format(url, uid)).json()
    with open("{}.csv".format(uid), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([uid, user.get("username"), t.get("completed"),
                           t.get("title")])
