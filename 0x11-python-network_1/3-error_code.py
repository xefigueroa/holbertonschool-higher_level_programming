#!/usr/bin/python3
"""takes URL, sends request to URL and displays the response"""
import urllib.error as error
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
