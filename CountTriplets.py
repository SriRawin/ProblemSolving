import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.


def countTriplets(arr, r):
    count = 0
    pairs={}
    c = Counter(arr)
    for key in reversed(arr):
        if key*r in c.keys():
            count += c[key*r]
    print(count)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
