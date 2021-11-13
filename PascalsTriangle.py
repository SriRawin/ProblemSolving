def pascalsTriangle():
    numRows = 5
    pascalList = []
    for i in range(0, numRows):
        pascalList.append([1]*(i+1))
        if len(pascalList[i]) > 2:
            for k in range(len(pascalList[i-1])-1):
                pascalList[i][k+1] = pascalList[i-1][k]+pascalList[i-1][k+1]

    print(pascalList)


pascalsTriangle()
