import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    k1=x1
    k2=x2
    for i in range(max(x1,x2,v1,v2)):
        k1+=v1
        k2+=v2
        print(k1,k2)
        if k1==k2:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()