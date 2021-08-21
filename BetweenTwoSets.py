import math
import os
import random
import re
import sys
from typing import Counter

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    count = 0
    factors_list = [max(a)*i for i in range(1, (min(b)//max(a)) + 1)]

    result_list = []
    
    for factor in factors_list:
        for a_item in a:
            if factor % a_item != 0:
                break
            result_list.append(factor)
    c = Counter(result_list)
    final_list = []
    final_list = [key for key, value in c.items() if value == len(a)]
    count_list=[]
    for item in final_list:
        for b_item in b:
            if b_item % item != 0:
                break
            count_list.append(item)
    count_dict=Counter(count_list)
    return sum([1 for key,value in count_dict.items() if value == len(b)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
