#!/usr/bin/python3
"""Module returns the list of users to-do list progress."""

import csv
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

    with open(f"{employee_id}.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)

        for task in todo_data:
            task_list = [
                employee_id, employee_username,
                task.get("completed", False),
                task.get("title")
                ]
            csv_writer.writerow(task_list)


if __name__ == "__main__":
    # Check if the number of command line arguments are meet
    if len(sys.argv) != 2:
        print("MODULE USAGE:")
        print("\t run: .\\0-gather_data_from_an_API <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_list_progress_csv(employee_id)
