
import math
import os
import random
import re
import sys


def lilysHomework(arr):
    swaps = 0
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if arr[j] <= arr[i]:
                minimum = j
        if i != minimum:
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
