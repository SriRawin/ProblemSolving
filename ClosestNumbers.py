import math
import os
import random
import re
import sys


def closestNumbers(arr):
    difference = None
    arr.sort()
    result_list = []
    for i in range(len(arr)-1):
        curr_difference = abs(arr[i]-arr[i+1])
        if not difference:
            difference = curr_difference
            result_list.append(arr[i])
            result_list.append(arr[i+1])
        elif curr_difference <= difference:
            difference = curr_difference
            while result_list and (abs(result_list[-1]-result_list[-2]) != difference):
                result_list.pop()
                result_list.pop()
            result_list.append(arr[i])
            result_list.append(arr[i+1])

    return result_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
