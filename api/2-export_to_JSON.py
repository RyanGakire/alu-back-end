#!/usr/bin/python3
"""
Uses a REST API to export all TODO tasks of an employee to a JSON file.

Usage: ./2-export_to_JSON.py <employee_id>
The file is saved as <employee_id>.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": employee_id}).json()

    username = user.get("username")

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({employee_id: tasks}, json_file)
