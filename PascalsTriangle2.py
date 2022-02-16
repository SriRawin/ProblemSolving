def getRow( rowIndex):
    n=rowIndex+1
    pascalList=[]
    for i in range(n):
        pascalList.append([1]*(i+1))
        if i>1:
            for j in range(len(pascalList[i-1])-1):
                pascalList[i][j+1]=pascalList[i-1][j]+pascalList[i-1][j+1]
    return pascalList[-1]