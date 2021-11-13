def reshapedMatrix():
    mat = [[1, 2, ], [3, 4]]
    r = 4
    c = 1
    rows = len(mat)
    columns = len(mat[0])
    if r*c != rows*columns:
        return mat
    else:
        reshapedMat = []
        temp = []
        for i in range(rows):
            for j in range(columns):
                temp.append(mat[i][j])
        print(temp)
        for x in range(0, r):
            reshapedMat.append(temp[x*c:c*(x+1)])
        print(reshapedMat)


reshapedMatrix()
