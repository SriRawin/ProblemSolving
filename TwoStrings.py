import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    result = set.intersection(s1_set, s2_set)
    return "YES" if len(result)>0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
