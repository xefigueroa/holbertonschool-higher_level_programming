#!/usr/bin/python3
"""script takes URL/email, sends POST req to passed URL w/ email as param"""
import urllib.parse as parse
import urllib.request as request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
