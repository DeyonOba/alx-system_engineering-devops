#!/usr/bin/python3
"""Module returns the list of users to-do list progress."""

import os
import requests
import sys


def get_todo_list_progress_csv(employee_id):
    """Save employee to-do list progress as a CSV file.

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
    total_tasks = len(todo_data)
    num_complete_tasks = sum(task.get('completed') for task in todo_data)

    for task in todo_data:
        task_completed_status = task.get("completed", False)
        task_title = task.get("title")

        with open(f"{employee_id}.csv", "a") as file:
            file.writelines(",".join([
                str(employee_id), employee_username,
                str(task_completed_status), task_title
            ]))
            file.write("\n")


if __name__ == "__main__":
    # Check if the number of command line arguments are meet
    if len(sys.argv) != 2:
        print("MODULE USAGE:")
        print("\t run: .\\0-gather_data_from_an_API <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_list_progress_csv(employee_id)
