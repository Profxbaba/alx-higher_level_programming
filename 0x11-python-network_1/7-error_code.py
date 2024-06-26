#!/usr/bin/python3
"""
Module: 7-error_code.py

Python script that takes in a URL, sends a request, and displays the body of
the response. If the HTTP status code is greater than or equal to 400, prints:
Error code: followed by the value of the HTTP status code.

Uses only the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
