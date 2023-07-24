#!/usr/bin/python3
"""Return info on employee to-do list progress using REST API"""

import requests
from sys import argv


if __name__ == '__main__':
    employee_ID = int(argv[1])

    empName = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(employee_ID)).json().get("name")
    tasks = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(employee_ID)).json()

    completedTasks = []
    for task in tasks:
        if task["completed"]:
            completedTasks.append(task["title"])

    print("Employee {} is done with tasks({:d}/{:d})"
          .format(empName, len(completedTasks), len(tasks)))

    for task in completedTasks:
        print("\t {}".format(task))
