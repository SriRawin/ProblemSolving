import math
import os
import random
import re
import sys
from collections import Counter


def countSort(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i][1] = "-"
    c = Counter([arr[x][0] for x in range(n)])
    arr_max = max(c.keys())
    print(c)
    init_arr = [None]*(int(arr_max)+1)
    for i in range(len(init_arr)):
        init_arr[i] = c[str(i)] if c[str(i)] else 0
    print(init_arr)
    count_arr = [init_arr[0]]
    for i in range(1, len(init_arr)):
        count_arr.append(count_arr[i-1]+init_arr[i])
    print(count_arr)
    shift_arr = [0]
    for i in range(len(count_arr)-1):
        shift_arr.append(count_arr[i])
    print(shift_arr)
    sorted_arr = [None]*n
    for i in range(n):
        sorted_arr[shift_arr[int(arr[i][0])]] = arr[i][1]
        shift_arr[int(arr[i][0])] += 1
    print(*sorted_arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
