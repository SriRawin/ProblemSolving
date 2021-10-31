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

    final_arr = [None]*len(arr)
    for x in range(len(arr)):
        final_arr[shift_arr[arr[x]]] = arr[x]
        shift_arr[arr[x]] += 1

    return final_arr


def activityNotifications(expenditure, d):
    notifications = 0
   
    k = len(expenditure)-d
    for i in range(k):
        curr_expense = expenditure[i:d]
        curr_expense = countingSort(curr_expense)

        mid_point = len(curr_expense)//2
       
        if len(curr_expense) % 2 != 0:
            median = curr_expense[mid_point]
        else:
            median = (curr_expense[mid_point]+curr_expense[mid_point-1])/2
       
        if expenditure[d] >= (2*median):
            notifications += 1

        k += 1
        d += 1
   
    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
