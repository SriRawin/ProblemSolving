import math
import os
import random
import re
import sys
from collections import Counter


def countingSort(arr):
    n = 100
    result = [0]*n
    c = Counter(arr)
    for i in range(n):
        result[i] = c[i] if c[i] else 0
    
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
