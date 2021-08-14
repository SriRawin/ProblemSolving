import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def createDict(s):
    s_dict={}
    for key in s:
        if key in s_dict.keys():
            s_dict[key]+=1
        else:
            s_dict.update({key:1})
    return s_dict
    
def anagram(s):
    
    if len(s)%2 != 0:
        return -1
    else:
        count=0
        mid_point=len(s)//2
        s1=s[:mid_point]
        s2=s[mid_point:]
        s1_dict=createDict(s1)
        s2_dict=createDict(s2)
        for key in s2_dict.keys():
            if key not in s1_dict.keys():
                count+=max(0,s2_dict[key]) if s2_dict[key] > 1 else 1
            else:
                count+=max(0,s2_dict[key]-s1_dict[key])
        
        return count

    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
