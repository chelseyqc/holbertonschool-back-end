#!/usr/bin/python3
"""
returns info about an employee's todo list progress based on id,
exports data in the csv format
"""
import csv
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
    # open csv file to write
    with open('{}.csv'.format(USER_ID), mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # write rows in required format
        for todo in todos_list:
            TASK_COMPLETED_STATUS = todo['completed']
            TASK_TITLE = todo['title']
            writer.writerow([USER_ID,
                            USERNAME,
                            TASK_COMPLETED_STATUS,
                            TASK_TITLE])
