#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status."""
import urllib.request as request


if __name__ == "__main__":
    "https://intranet.hbtn.io/status"
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
