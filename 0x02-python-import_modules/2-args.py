#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    if argc <= 1:
        print("{} arguments.".format(argc - 1))
    elif argc == 2:
        print("{} argument:".format(argc - 1))
        for index, item in enumerate(argv[1:]):
            print("{}: {}".format(index + 1, item))
    else:
        print("{} arguments:".format(argc - 1))
        for index, item in enumerate(argv[1:]):
            print("{}: {}".format(index + 1, item))
