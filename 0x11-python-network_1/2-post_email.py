#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
"""

import urllib.parse
import urllib.request
import sys


def post_email(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to include as a parameter in the request.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
