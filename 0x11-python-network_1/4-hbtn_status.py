#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    txt = r.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
