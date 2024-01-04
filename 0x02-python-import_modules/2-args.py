#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argcount = len(argv) - 1

    if argcount == 0:
        print("{} arguments.".format(argcount))
    elif argcount == 1:
        print("{} argument:".format(argcount))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argcount))
        for i in  range(1, argcount + 1):
            print("{}: {}".format(i, argv[i]))
