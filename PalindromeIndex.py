import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    for index in range(len(s)//2):
        if s[index] != s[-index-1]:
            if s[index+1] == s[-index-1] and s[index+2]==s[-index-2]:
                return index
            elif s[index]==s[-index-2] and s[index+1] ==s[-index-3]:
                return len(s)-(index+1)
    
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
