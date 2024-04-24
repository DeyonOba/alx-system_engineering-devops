#!/usr/bin/python3
"""Module saves the list of users to-do list progress in a JSON file.

file format: <employee_id>.json
content:
- {"USER_ID": [{
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
      "username": "USERNAME"}, ...
      }]
}
"""

import json
import requests
import sys


def get_todo_list_progress_json(employee_id):
    """Save employee to-do list progress as a JSON file.

    Parameters:
    - employee_id(int): Employee unique identifier

    Returns:
    - None
    """
    employee_id = int(employee_id)

    # store URL's
    web_url = "https://jsonplaceholder.typicode.com"
    user_var = "users"
    user_data_url = "/".join([web_url, user_var, str(employee_id)])
    todo_list_url = "/".join([user_data_url, f"todos?userId={employee_id}"])

    # Make user and to-do list requests
    user_request = requests.get(user_data_url)
    todo_list_request = requests.get(todo_list_url)

    # Store employee  and to-do list data as dict
    employee_data = user_request.json()
    todo_data = todo_list_request.json()

    # Extract employee info
    employee_username = employee_data.get('username')

    task_list = []
    for task in todo_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed", False),
            "username": employee_username
        }
        task_list.append(task_info)

    user_todo_details = {str(employee_id): task_list}

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(user_todo_details, json_file)


if __name__ == "__main__":
    # Check if the number of command line arguments are meet
    if len(sys.argv) != 2:
        print("MODULE USAGE:")
        print("\t run: .\\0-gather_data_from_an_API <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_list_progress_json(employee_id)
