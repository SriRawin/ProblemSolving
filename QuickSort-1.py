import math
import os
import random
import re
import sys


def sort(start, end, arr):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end and start != end:
            arr[start], arr[end] = arr[end], arr[start]
    if pivot_index != end:
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return end


def quickSort(start, end, arr):
    if start < end:
        pivot_index = sort(start, end, arr)
        quickSort(start, pivot_index-1, arr)
        quickSort(pivot_index+1, end, arr)
  


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(0, len(arr)-1, arr)
    print(arr)
