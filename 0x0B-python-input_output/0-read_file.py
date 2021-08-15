#!/usr/bin/python3
"""text file reading function"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as _file:
        print(_file.read(), end="")
