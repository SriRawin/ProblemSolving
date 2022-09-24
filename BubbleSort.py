import math
import os
import random
import re
import sys



def bubbleSort(n, a):
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
                swapped = True
        if swapped == False:
            break
    print('Array is sorted in',swaps,'swaps.')
    print('First Element:',a[0])
    print('Last Element:',a[-1])


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    bubbleSort(n, a)
