import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    n=len(s)
    ascii_list=[ord(value) for value in s ]
    diff_list=[ abs(ascii_list[i]-ascii_list[i+1])- abs(ascii_list[(n-1)-i]-ascii_list[((n-1)-i)-1])  for i in range(n-1)]
    return 'Funny' if diff_list.count(0)==len(diff_list) else "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()