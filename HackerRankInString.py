import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    original_String="hackerrank"
    string_list=list(s)
    new_string=""
    for i in range(len(original_String)):
        for j in range(len(string_list)):
            if original_String[i]==string_list[j]:
                new_string+=string_list[j]
                del string_list[:j+1]
                break
            

    return "YES" if new_string==original_String else "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()