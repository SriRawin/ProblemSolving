

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    add_on_char=n%len(s)
    repetitions=n//len(s)
    stringCounter=(s.count("a")*repetitions)+(s[:add_on_char].count("a"))
    return stringCounter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()