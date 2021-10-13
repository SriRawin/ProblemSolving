import math
import os
import random
import re
import sys


def equalStacks(h1, h2, h3):
    s1, s2, s3 = map(sum, (h1, h2, h3))
    if s1 == s2 == s3:
        return s1
    while h1 and h2 and h3:
        minimum = min(s1, s2, s3)
        if s1 > minimum:
            s1 -= h1.pop(0)
        if s2 > minimum:
            s2 -= h2.pop(0)
        if s3 > minimum:
            s3 -= h3.pop(0)
        if s1 == s2 == s3:
            return s1

    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
