import math
import os
import random
import re
import sys
from collections import Counter


def pickingNumbers(a):
    result = 0
    c = Counter(a)
    dict_key = list(c.keys())
    print(c)
    for i in range(len(dict_key)):
        if (dict_key[i]-1) or dict_key[i] in dict_key:
            sum = c[dict_key[i]] + c[dict_key[i]-1]
            result = sum if sum > result else result
    print(result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
