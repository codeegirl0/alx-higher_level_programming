i#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for myrow in matrix:
        for mycol in myrow:
            print("{:d}".format(mycol), end=" " if mycol != myrow[-1] else "")
        print()
