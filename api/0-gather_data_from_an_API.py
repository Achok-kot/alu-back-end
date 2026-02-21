#!/usr/bin/python3
"""Script to fetch employee TODO list progress from REST API"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    
    completed = [task for task in todos if task.get("completed")]
    
    print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)}):")
    for task in completed:
        print(f"\t {task.get('title')}")
