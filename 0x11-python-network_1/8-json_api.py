#!/usr/bin/python3
"""
Module: 8-json_api.py

Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id
and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty

Uses only the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    try:
        response = requests.post(url, data={'q': q}).json()
        if response:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
