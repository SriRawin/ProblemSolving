import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def superReducedString(s):
    string_list = [i for i in s]
    reduced_String = ""
    count = 0
    while(count < len(string_list) and count+1 < len(string_list)):

        if string_list[count] == string_list[count+1]:
            del string_list[count], string_list[count]
            count = 0
        else:
            count+=1
      

        
    
    for i in string_list:
        reduced_String += i

    return reduced_String if len(reduced_String) != 0 else "Empty String"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
