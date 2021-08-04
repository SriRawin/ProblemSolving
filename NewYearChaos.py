import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes=0
    for original , current in enumerate(q,1):
        if current - original > 2:
            print ( "Too chaotic")
            return
        for i in range ( max(current-2,0),original):
            if q[i]>current:
                bribes+=1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)