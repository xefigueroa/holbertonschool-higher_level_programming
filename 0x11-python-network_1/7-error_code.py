#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the URL with the email and
displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
