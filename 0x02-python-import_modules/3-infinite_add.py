#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]

    if len(argv) == 0:
        print("{}".format(0))
    else:
        sum = 0
        for i in argv:
            sum += int(i)
        print("{}".format(sum))
