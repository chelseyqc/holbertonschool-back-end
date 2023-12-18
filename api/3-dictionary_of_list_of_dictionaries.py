#!/usr/bin/python3
"""
returns info about all employee's todo list progress,
exports data in the json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    # Base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # fetching user data
    users_url = base_url + "/users"
    user_data = requests.get(users_url).json()

    all_tasks = {}

    # fetching tasks and todos
    for user in user_data:
        USERNAME = user['username']
        USER_ID = user['id']

        # fetching todos for the user
        todos_url = base_url + "/users/" + str(USER_ID) + "/todos"
        todos_list = requests.get(todos_url).json()

        # json export data
        tasks = [{
            "username": USERNAME,
            "task": todo['title'],
            "completed": todo['completed']
        } for todo in todos_list]

        all_tasks[USER_ID] = tasks

    # write data to json
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
