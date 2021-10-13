import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#


def getMax(operations):
    stack = deque()
    result_list = []
    maximum = 0
    for operation in operations:
        operation = operation.split(" ")
        if operation[0] == '1':
            stack.append(int(operation[1]))
            if int(operation[1]) > maximum:
                maximum = int(operation[1])
        elif operation[0] == '2':
            stack.pop()
            if len(stack) == 0:
                maximum = 0
            else:
                maximum = max(stack)
        else:
            result_list.append(maximum)
    return result_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
