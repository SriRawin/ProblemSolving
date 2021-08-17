import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    c = Counter(s)
    single_count = 0
    value_list = list(c.values())
    for value in value_list:
        if value_list[0] != value:
            single_count += 1
            
        

    return 'YES' if single_count <= 1 else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
