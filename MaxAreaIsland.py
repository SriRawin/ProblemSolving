visited = set()
curr = 0


def dfs(grid, r, c):
    global curr
    curr += 1
    print(curr)
    visited.add((r, c))
    if r-1 >= 0 and grid[r-1][c] == 1 and (r-1, c) not in visited:
        dfs(grid, r-1, c)
    if r+1 < len(grid) and grid[r+1][c] == 1 and (r+1, c) not in visited:
        dfs(grid, r+1, c)
    if c-1 >= 0 and grid[r][c-1] == 1 and (r, c-1) not in visited:
        dfs(grid, r, c-1)
    if c+1 < len(grid[0]) and grid[r][c+1] == 1 and (r, c+1) not in visited:
        dfs(grid, r, c+1)


def main():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            global curr 
            curr = 0
            if grid[i][j] == 1:
                if (i, j) not in visited:
                    dfs(grid, i, j)
                    print(curr, visited)


main()
