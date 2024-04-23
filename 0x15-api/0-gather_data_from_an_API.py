#!/usr/bin/python3
"""Module returns the list of users to-do list progress."""

import requests
import sys


def get_todo_list_progress(employee_id):
    """Get users to do list progress.

    Parameters:
    - employee_id(int): Employee unique identifier

    Returns:
    - None
    """
    # store URL's
    web_url = "https://jsonplaceholder.typicode.com"
    user_var = "users"
    user_data_url = "/".join([web_url, user_var, str(employee_id)])
    todo_list_url = "/".join(
        [user_data_url, f"todos?userId={str(employee_id)}"])

    # Make user and to-do list requests
    user_request = requests.get(user_data_url)
    todo_list_request = requests.get(todo_list_url)

    # Store employee  and to-do list data as dict
    employee_data = user_request.json()
    todo_data = todo_list_request.json()

    # Extract employee info
    employee_name = employee_data.get('name')
    total_tasks = len(todo_data)
    num_complete_tasks = sum(task.get('completed') for task in todo_data)

    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, num_complete_tasks, total_tasks
    ))
    # Display title of completed tasks
    for task in todo_data:
        if task.get('completed', False):
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    # Check if the number of command line arguments are meet
    if len(sys.argv) != 2:
        print("MODULE USAGE:")
        print("\t run: .\\0-gather_data_from_an_API <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_list_progress(employee_id)
