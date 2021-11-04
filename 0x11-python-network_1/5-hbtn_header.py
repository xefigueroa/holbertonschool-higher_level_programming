#!/usr/bin/python3
"""takes URL, sends request to URL and displays value of variable X-Request-Id"""
import requests as r
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    print(r.get(url).headers.get("X-Request-Id"))
