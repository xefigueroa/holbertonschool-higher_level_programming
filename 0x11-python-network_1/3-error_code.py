#!/usr/bin/python3
"""takes URL, sends request to URL and displays the response"""
import urllib.error as error
import urllib.request as request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
