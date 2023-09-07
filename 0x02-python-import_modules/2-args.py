#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    if argc == 1:
        print(f"{argc - 1} arguments.")
    else:
        print(f"{argc - 1} argument:")
        for index,item in enumerate(argv[1:]):
            print("{}: {}".format(index + 1, item))

