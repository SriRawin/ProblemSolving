import math
import os
import random
import re
import sys

def insertionSort(arr):
    shifts=0
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while arr[j]>key and j>=0:
            arr[j+1]=arr[j]
            shifts+=1
            j-=1
        arr[j+1]=key
    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()