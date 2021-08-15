import math
import os
import random
import re
import sys
from collections import Counter


def create_ss(s):
    ss_list = [char for char in s]
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            ss_list.append("".join(sorted(s[i:j+1])))
    return Counter(ss_list)



def sherlockAndAnagrams(s):
    ss_list = create_ss(s)
    count = 0
    for key in ss_list.keys():
        if ss_list[key]>1:
            count+=(ss_list[key] *( ss_list[key]-1))//2
    print(count)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
