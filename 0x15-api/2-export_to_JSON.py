#!/usr/bin/python3
"""Return info on employee to-do list progress using REST API
   Store as JSON string"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    try:
        employee_ID = int(argv[1])
    except ValueError:
        print("Argument should be an integer")
        exit(1)

    empName = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(employee_ID)).json().get("username")
    tasks = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(employee_ID)).json()

    listValue = []
    for task in tasks:
        content = {}
        content["task"] = task["title"]
        content["completed"] = task["completed"]
        content["username"] = empName
        listValue.append(content)

    myDict = {argv[1] : listValue}
    with open('{}.json'.format(employee_ID), 'w') as myJSON:
          json.dump(myDict, myJSON)
