#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Get TODO list
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    # Count completed tasks
    completed_tasks = sum(1 for task in todos_data if task["completed"])

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{len(todos_data)}):")
    for task in todos_data:
        if task["completed"]:
            print(f"\t{task['title']}")

