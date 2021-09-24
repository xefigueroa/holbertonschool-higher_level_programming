#!/usr/bin/python3
"""script takes URL/email, sends POST req to passed URL w/ email as param"""
import urllib.parse as parse
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    v = {'email': argv[2]}
    data = parse.urlencode(v).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
