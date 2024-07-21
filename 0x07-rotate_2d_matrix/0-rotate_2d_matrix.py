#!/usr/bin/python3
"""
rotating a 2-D matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    # transpose it first, would be teh other way around if counter clockwise
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):

            # swapp mat[i][j] and mat[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # since its clockwise and not counter clockwise, this comes last
    for i in range(len(matrix)):
        matrix[i].reverse()
