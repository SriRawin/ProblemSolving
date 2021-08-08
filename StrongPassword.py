import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # creiteria=0
    # to_be_added=0
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    specialChar = "!@#$%^&*()-+"
    numbers = "0123456789"
    password_dict = {
    "upper_Case": 0, "lower_Case": 0, "num": 0, "special_char": 0}
    for i in range(len(password)):
        if password[i] in upperCase:
            password_dict["upper_Case"] += 1
        elif password[i] in lowerCase:
            password_dict["lower_Case"] += 1
        elif password[i] in numbers:
            password_dict["num"] += 1
        elif password[i] in specialChar:
            password_dict["special_char"] += 1
    result = list(map(int,password_dict.values()))
    if n>=6:
        return result.count(0)
    else:
        # to_be_added=6-n
        # creiteria=result.count(0)
        return max(6-n,result.count(0))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
