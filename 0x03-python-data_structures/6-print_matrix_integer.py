#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for item in matrix:
            for idx, it in enumerate(item):
                print("{:d}".format(it), end="")
                if idx != 2:
                    print(end=" ")
            print()
