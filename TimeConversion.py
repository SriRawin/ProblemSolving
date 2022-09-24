import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    time_hour=int(s[:2])
    # converted_time=str(time_hour)+":"+s[3:5]+":"+s[6:8]
    if "PM" in s:
        if time_hour<12:
            time_hour+=12
            return str(time_hour)+":"+s[3:5]+":"+s[6:8]
        else:
            return s[:8]
    if "AM" in s:
        if time_hour<12:
            return s[:8]
        else:
            time_hour-=12
            return str(0)+str(time_hour)+":"+s[3:5]+":"+s[6:8]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()