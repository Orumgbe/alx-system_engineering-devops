#!/usr/bin/python3
"""Return info on employee to-do list progress using REST API
   Export data in CSV format"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    try:
        employee_ID = int(argv[1])
    except ValueError:
        print("Argument should be an integer")
        exit(1)

    empName = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(employee_ID)).json().get("name")
    tasks = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(employee_ID)).json()

    completedTasks = []

    with open('{}.csv'.format(employee_ID), 'w') as myCSV:
        fileLog = csv.writer(myCSV, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        for task in tasks:
            fileLog.writerow([employee_ID, empName, task["completed"],
                              task["title"]])
