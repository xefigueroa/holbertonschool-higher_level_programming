#!/usr/bin/python3
"""takes URL/email, sends POST req to passed URL w/ email as param, displays response."""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    print(requests.post(url, data=email).text)
