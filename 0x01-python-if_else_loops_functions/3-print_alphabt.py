#!/usr/bin/python3
for x in range(97, 123):
    if chr(x) is not 'q' and chr(x) is not 'e':
        print("{:c}".format(x), end="")
