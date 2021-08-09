import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def alternate(s):
    str_list = list(set(s))
    length=0
    for x in range(len(str_list)-1):
        for y in range(x+1, len(str_list)):
            possible_set = [item for item in s if item ==
                            str_list[x] or item == str_list[y]]
            if check(possible_set) :
                length=max(length,len(possible_set))
    return length
def check(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return False
    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
