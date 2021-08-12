import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    magazine_dict={}
    for key in magazine:
        if key in magazine_dict:
            magazine_dict[key]+=1
        else:
            magazine_dict.update({key:1})
    print(magazine_dict)
    for item in note:
        if item in magazine_dict and magazine_dict[item] >= 1:
            magazine_dict[item] -=1
        else:
            print("No")
            return
    print("Yes")
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)