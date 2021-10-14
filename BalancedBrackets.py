import math
import os
import random
import re
import sys
from collections import Counter


def isBalanced(s):
    if len(s) % 2 != 0:
        return "NO"

    bracket_dict = {"{": "}", "[": "]", "(": ")"}
    if s[0] in bracket_dict.values():
        return "NO"

    c = Counter(s)
    for key in bracket_dict.keys():
        if c[key] != c[bracket_dict[key]]:
            return "NO"

    i = 0
    j = i+1
    while j < len(s):
        if s[i] in bracket_dict.keys() and s[j] in bracket_dict.values():
            if bracket_dict[s[i]] != s[j]:
                return "NO"
        i = j
        j += 1

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
