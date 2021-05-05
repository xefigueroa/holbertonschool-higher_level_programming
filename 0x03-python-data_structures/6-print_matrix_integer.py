#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for v in range(len(matrix)):
        for w in range(len(matrix[v])):
            print("{:d}".format(matrix[v][w]), end="")
            if w != (len(matrix[v]) - 1):
                print(" ", end="")
        print("")
