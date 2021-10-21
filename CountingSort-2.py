
import math
import os
import random
import re
import sys
from collections import Counter


def countingSort(arr):
    arr_max = max(arr)
    n = arr_max+1
    init_arr = [0]*n
    c = Counter(arr)
    for i in range(n):
        init_arr[i] = c[i] if c[i] else 0
    count_arr = [init_arr[0]]
    count_start = count_arr[0]
    for j in range(1, n):
        count_start = count_arr[j-1]+init_arr[j]
        count_arr.append(count_start)
    shift_arr = [0]*n
    for k in range(1, n):
        shift_arr[k] = count_arr[k-1]
    print(shift_arr)
    final_arr = [None]*len(arr)
    for x in range(len(arr)):
        final_arr[shift_arr[arr[x]]] = arr[x]
        shift_arr[arr[x]] += 1
        

    return final_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
