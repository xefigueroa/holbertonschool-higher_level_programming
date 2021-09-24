#!/usr/bin/python3
"""makes URL, sends request to URL and displays value of X-Request-Id"""
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    r = request.Request(argv[1])
    with request.urlopen(r) as response:
        print(response.headers.get('X-Request-Id'))
