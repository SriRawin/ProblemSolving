import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#


def isPalindrome(s):
    return True if s == s[::-1] else False

def palindromeResult(s_list,k,n,o_list):
    for i in range(n//2):
        if o_list[i]!=o_list[-i-1] and o_list[i] != "9" and o_list[-i-1] != "9":
            s_list[i] = "9"
            s_list[-i-1] = "9"
            k -= 1

        elif s_list[i] != "9" and k >= 2:
            s_list[i] = "9"
            s_list[-i-1] = "9"
            k -= 2
    if n%2 != 0 and k>0:
            s_list[n//2] = "9"
            k -= 1
    result="".join(s_list)
    return result

def makePalindrome(s_list,n,k,o_list):
    c=0
    for i in range(n//2):
        if ( s_list[i] != s_list[-i-1] ):
            if s_list[i] > s_list[-i-1] :
                k-=1
                s_list[-i-1] = s_list[i]
            if s_list[-i-1] > s_list[i] :
                s_list[i] = s_list[-i-1]
                k-=1
                
    result="".join(s_list)
    if k<0:
        return "-1"

   
    if isPalindrome(result):
        return palindromeResult(s_list,k,n,o_list)
    


def highestValuePalindrome(s, n, k):
    s_list = list(s)
    o_list=list(s)

    if isPalindrome(s):
        return palindromeResult(s_list,k,n,o_list)

    else:
        return makePalindrome(s_list,n,k,o_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
