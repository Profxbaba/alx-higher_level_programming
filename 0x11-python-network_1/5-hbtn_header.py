#!/usr/bin/python3
"""
Module: 5-hbtn_header.py

Python script that fetches a URL, sends a request, and displays the value
of the variable X-Request-Id in the response header.

Uses only requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
