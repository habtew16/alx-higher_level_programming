#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for it in item:
            print("{:d}".format(it), end="")
            if it is not item[len(item) - 1]:
                print(" ", end="")
        print()
