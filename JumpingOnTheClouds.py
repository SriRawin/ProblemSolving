
import math
import os
import random
import re
import sys



def jumpingOnClouds(c):
    jumps=0
    i=0
    j=0
    while i < len(c):
        j=i+1
       
        while j < len(c):
            
            if c[j]==0:
                if (j+1 ) < len(c) and c[j+1]==0:
                    i=j+1
                    j=i+1
                    jumps=jumps+1
                else:
                    i=j
                    j=i+1
                    jumps=jumps+1
            elif c[j]==1:
                i=j+1
                j=i+1
                jumps=jumps+1
        break
   
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
