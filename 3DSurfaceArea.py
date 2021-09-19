import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#


def surfaceArea(A):
    area = len(A)*len(A[0])*2
    a = [[0] * (len(A[0])+2)]
    for r in A:
        a.append([0]+r+[0])
    a.append([0]*(len(A[0])+2))
    print(a)
    for i in range(1, len(a)):
        for j in range(1, len(a[0])):
            area += abs(a[i][j]-a[i-1][j])

            area += abs(a[i][j]-a[i][j-1])
    print(area)
    return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
