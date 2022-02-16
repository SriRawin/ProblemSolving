def rotate(matrix):
    m = len(matrix)
    for i in range(m):
        for j in range(i, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(m):
        for j in range(m//2):
            matrix[i][j], matrix[i][-(j+1)] = matrix[i][-(j+1)], matrix[i][j]
    print(*matrix)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
