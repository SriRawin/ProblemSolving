import math
import os
import random
import re
import sys


def counterGame(n):
    count = 0
    while n > 1:
        curr = (n & n-1)
        if curr == 0:
            n //= 2
        else:
            n -= curr
        print(curr, n)
        count += 1
        print(count)
    print("Richard" if count % 2 == 0 else "Louise")
    return "Richard" if count % 2 == 0 else "Louise"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
