def island_perimeter(grid):
    """function to return the perimeter of an island"""
    row = len(grid)
    col = len(grid[0])
    perm = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                perm = perm + 4

                if i > 0 and grid[i - 1][j] == 1:
                    perm = perm - 2
                if j > 0 and grid[i][j - 1] == 1:
                    perm = perm - 2
    return (perm)
