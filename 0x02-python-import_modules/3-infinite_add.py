#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tot = 0
    for x in range(len(sys.argv) - 1):
        tot = tot + int(sys.argv[x + 1])
    print(tot)
