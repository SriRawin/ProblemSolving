def search2dMatrix():
    matrix = [[1], [3]]
    target = 3
    # maybe = 0
    # for i in range(len(matrix)):
    #     if target > matrix[i][0] and target < matrix[i][-1]:
    #         maybe = i
    #         break
    # for item in matrix[maybe]:
    #     if item == target:
    #         print(True)
    #         return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                print(True)
                return
    print(False)


search2dMatrix()
