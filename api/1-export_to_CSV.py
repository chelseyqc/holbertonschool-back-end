#!/usr/bin/python3
"""
returns info about an employee's todo list progress based on id,
exports data in the csv format
"""
import requests
import sys
import csv


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
    users = requests.get(users_url).json()
    USER_ID = users['id']
    # open csv file to write
    with open('{}.csv'.format(USER_ID), mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # write rows in required format
        for todo in todos_list:
            USERNAME = users['username']
            TASK_COMPLETED_STATUS = todo['completed']
            TASK_TITLE = todo['title']
            writer.writerow([USER_ID,
                            USERNAME,
                            TASK_COMPLETED_STATUS,
                            TASK_TITLE])
