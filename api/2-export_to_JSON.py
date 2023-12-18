#!/usr/bin/python3
"""
returns info about an employee's todo list progress based on id,
exports data in the json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    # Base URL
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = str(sys.argv[1])

    # fetching user data
    users_url = base_url + "/users/" + employee_id
    user_data = requests.get(users_url).json()
    EMPLOYEE_NAME = user_data.get('name')
    USERNAME = user_data.get('username')
    USER_ID = user_data['id']

    # fetching todos
    todos_url = base_url + "/users/" + employee_id + "/todos"
    todos_list = requests.get(todos_url).json()
    TOTAL_NUMBER_OF_TASKS = len(todos_list)
    NUMBER_OF_DONE_TASKS = len([todo for todo in todos_list
                                if todo['completed']])

    # json export data
    tasks = [{
        "task": todo['title'],
        "completed": todo['completed'],
        "username": USERNAME
    } for todo in todos_list]

    todos_data = { USER_ID: tasks }

    # write data to json
    with open("{}.json".format(USER_ID), 'w') as jsonfile:
        json.dump(todos_data, jsonfile)
