import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    alphabet_dict={key : 0 for key in alphabets}
    for char in s:
        alphabet_dict[char]+=1
    return "pangram" if 0 not in alphabet_dict.values() else "no pangram"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s.replace(" ","").lower())

    fptr.write(result + '\n')

    fptr.close()