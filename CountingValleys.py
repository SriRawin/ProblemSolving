

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    
    valleyCounter=0
    unit=0
    for i in range(0,steps):
        if path[i] == "D":
            unit=unit-1
        elif path[i] == "U":
            unit= unit + 1
            if unit==0:
                valleyCounter=valleyCounter+1
            
    return valleyCounter
        

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()