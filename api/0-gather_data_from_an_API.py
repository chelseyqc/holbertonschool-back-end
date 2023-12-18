#!/usr/bin/python3
"""returns info about an employee's todo list progress based on id"""
import requests
import sys


if __name__ == "__main__":
    # Base URL
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = str(sys.argv[1])
    users_url = base_url + "/users/" + employee_id
    EMPLOYEE_NAME = requests.get(users_url).json().get('name')

    todos_url = base_url + "/users/" + employee_id + "/todos"
    todos_list = requests.get(todos_url).json()
    TOTAL_NUMBER_OF_TASKS = len(todos_list)

    NUMBER_OF_DONE_TASKS = len([todo for todo in todos_list
                                if todo['completed']])

    # print progress
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
    ))

    # print title of completed tasks
    for todo in todos_list:
        if todo['completed']:
            print("\t {}".format(todo['title']))
