import math
import os
import random
import re
import sys


def introTutorial(V, arr):
    n = len(arr)
    i = 0
    while i < n:
        if V == arr[i]:
            return i
        i += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
