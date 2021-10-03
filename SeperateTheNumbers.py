import math
import os
import random
import re
import sys


def isSequential(s, sub_str):
    if not s:
        return True
    if s.startswith(sub_str):
        l = len(sub_str)
        return isSequential(s[l:], str(int(sub_str)+1))
    return False


def separateNumbers(s):
    for i in range(1, (len(s)//2)+1):
        sub_str = s[:i]
        if isSequential(s, sub_str):
            print("YES " + sub_str)
            return

    print('NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
