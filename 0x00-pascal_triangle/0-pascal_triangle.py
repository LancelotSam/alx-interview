#!/usr/bin/python3
"""
This module defines a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of height n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
