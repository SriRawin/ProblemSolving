import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minimum=arr[0]+arr[1]+arr[2]+arr[3]
    maximum=arr[4]+arr[1]+arr[2]+arr[3]
    print(minimum,maximum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)