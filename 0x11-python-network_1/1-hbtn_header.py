#!/usr/bin/python3
"""makes URL, sends request to URL and displays value of X-Request-Id"""
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
