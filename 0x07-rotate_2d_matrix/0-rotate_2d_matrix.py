#!/usr/bin/python3
"""model to rotate a 2d matrix"""


def rotate_2d_matrix(matrix):
    """function to rotate 2d matrix 90 degree clockwise"""
    matrix.reverse()
    for row in range(len(matrix)):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row],
            matrix[row][col]
