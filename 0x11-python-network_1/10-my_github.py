#!/usr/bin/python3
"""
Module: 10-my_github.py

Python script that takes GitHub credentials(username and personal access token)
and uses the GitHub API to display the user id.

Uses Basic Authentication with a personal access token as password to access
user information (only read:user permission is needed).

Uses only the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        print(data.get('id'))
    except ValueError:
        print("Not a valid JSON")
