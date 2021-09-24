#!/usr/bin/python3
"""takes URL/email, sends POST req to passed URL w/ email as param, displays response."""
import requests
from sys import argv


if __name__ == '__main__':
    v = {'email': argv[2]}
    r = requests.post(argv[1], data=v)
    print(r.text)
