#!/usr/bin/python3
"""
Module: 4-hbtn_status.py

Python script that fetches https://alx-intranet.hbtn.io/status using requests.
Displays the body of the response with specific formatting.

Uses only the requests package.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
