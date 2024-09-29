#!/usr/bin/python3
"""module to measure perimeter if island"""


def island_perimeter(grid):
    """function to return the perimeter of an island"""
    myrow = len(grid)
    mycol = len(grid[0])
    perm = 0

    for i in range(myrow):
        for j in range(mycol):
            if grid[i][j] == 1:
                perm = perm + 4

                if i > 0 and grid[i - 1][j] == 1:
                    perm = perm - 2
                if j > 0 and grid[i][j - 1] == 1:
                    perm = perm - 2
    return (perm)
