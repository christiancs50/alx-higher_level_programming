#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = argv[1:]

    sumargs = 0

    for args in args:
        sumargs += int(args)

    print(sumargs)
