#!/usr/bin/python3
"""Return info on employee to-do list progress using REST API
   Store as JSON string, this module saves data on all employees"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    employee_ID = 1
    allDict = {}
    allEmp = requests.get("https://jsonplaceholder.typicode.com/users").json()
    count = len(allEmp)

    while (employee_ID <= count):
        empName = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                               .format(employee_ID)).json().get("username")
        if (empName == ''):
            employee_ID += 1
            continue

        todoURL = "https://jsonplaceholder.typicode.com/users/{}/todos"\
                  .format(employee_ID)
        tasks = requests.get(todoURL).json()

        listValue = []
        for task in tasks:
            content = {}
            content["username"] = empName
            content["task"] = task["title"]
            content["completed"] = task["completed"]
            listValue.append(content)

        allDict[employee_ID] = listValue
        employee_ID += 1

    with open('todo_all_employees.json', 'a') as myJSON:
        json.dump(allDict, myJSON)
