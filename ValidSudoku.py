def validSudoku():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".",  "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"], ]

    for i in range(9):
        for j in range(9):
            if board[i][j] != "." and board[i].count(board[i][j]) > 1:
                print(False)
                return
    seen = []
    for i in range(9):
        for j in range(9):
            if board[j][i] != ".":
                if board[j][i] in seen:
                    print(False)
                    return
                else:
                    seen.append(board[j][i])
        seen = []
    subMatrix = []
    r = 3
    c = 3
    for i in range(9):
        for j in range(9):
            if i < r and j < r:
                subMatrix.append(board[i][j])

    seen = []
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y]
                      for x in range(i, i+3) for y in range(j, j+3)]
            for num in square:
                if num != ".":
                    if num in seen:
                        print(False)
                        return
                    else:
                        seen.append(num)
            seen = []

    print(True)


validSudoku()
