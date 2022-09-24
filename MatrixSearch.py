def searchMatrix(matrix,target):
    matrixLength=len(matrix)
    i=0
    while(i<matrixLength):
        if(target>=matrix[i][0] and target<=matrix[i][-1]):
            for num in matrix[i]:
                if(num == target):
                    return True
            break
        i+=1
    
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
result=searchMatrix(matrix,target)
print(result)