#!/usr/bin/python3
"""Script to send a request to a URL & display value of X-Request-Id header"""

import urllib.request
import sys


def display_x_request_id(url):
    """
    Sends a request to specified URL & displays value of X-Request-Id header

    Args:
        url (str): The URL to send the request to
    """
    with urllib.request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    display_x_request_id(url)
