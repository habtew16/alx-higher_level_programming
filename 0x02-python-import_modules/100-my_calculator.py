#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argc = len(argv)
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[0])
        op = argv[1]
        b = int(argv[2])
        if op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
            exit(0)
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
            exit(0)
        elif op == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
            exit(0)
        if op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
