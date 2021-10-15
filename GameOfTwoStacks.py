import math
import os
import random
import re
import sys


def twoStacks(maxSum, a, b):
    a = list(reversed(a))
    b = list(reversed(b))
  
    stack_sum = 0
    stack = []
    for _ in range(len(a)):
        top = a.pop()
        if top+stack_sum > maxSum:
            break
        stack_sum += top
        stack.append(top)
    max_score = len(stack)
    current_score = max_score
    b_len = len(b)
    while b_len:
        if stack_sum+b[-1] <= maxSum:
            stack_sum += b.pop()
            b_len -= 1
            current_score += 1
            if current_score > max_score:
                max_score = current_score
            continue
        if not len(stack):
            break
        val = stack.pop()
        stack_sum -= val
        current_score -= 1
    return max_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
