import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    s_ascii_list=[ord(i) for i in s]
    change_count=0
    for i in range(len(s)//2):
        change_count+=(abs(s_ascii_list[i]-s_ascii_list[-i-1]))
    print(change_count)
    return change_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()