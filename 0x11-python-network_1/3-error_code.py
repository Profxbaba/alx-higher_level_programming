#!/usr/bin/python3
"""
Module: 3-error_code.py

Python script that fetches a URL and prints the decoded body of the response.
Handles urllib.error.HTTPError and prints: Error code: followed by status code.

Uses urllib and sys.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
