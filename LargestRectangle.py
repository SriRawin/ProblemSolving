import math
import os
import random
import re
import sys


def largestRectangle(h):
    left_smaller = [None]*len(h)
    right_smaller = [None]*len(h)
    stack = []
    for i in range(len(h)):
        if not stack:
            stack.append(i)
            left_smaller[i] = stack[-1]
        else:
            if h[stack[-1]] < h[i]:
                left_smaller[i] = stack[-1]+1
                stack.append(i)
            else:
                for j in range(0, i):
                    if not stack:
                        left_smaller[i] = 0
                        break
                    if h[stack[-1]] >= h[i]:
                        if stack:
                            stack.pop()
                            continue
                    if h[stack[-1]] < h[i]:
                        left_smaller[i] = stack[-1]+1
                        stack.append(i)
                        break

                if not stack:
                    left_smaller[i] = 0
                    stack.append(i)

        print("i", i, "stack", stack)

    print(left_smaller)

    stack = []
    n = 0
    while n < len(h):
        i = (len(h)-n)-1
        if not stack:
            stack.append(i)
            right_smaller[i] = stack[-1]
        else:
            if h[i] > h[stack[-1]]:
                right_smaller[i] = stack[-1]-1
                stack.append(i)
            else:
                for j in range(i, (len(h)-1)):
                    if not stack:
                        right_smaller[i] = len(h)-1
                        break
                    if h[i] <= h[stack[-1]]:
                        if stack:
                            stack.pop()
                            continue

                    if h[i] > h[stack[-1]]:
                        right_smaller[i] = stack[-1]-1
                        stack.append(i)
                        break
                if not stack:
                    right_smaller[i] = len(h)-1
                    stack.append(i)

        n += 1
        print("i", i, "stack", stack)
    print(right_smaller)

    max_area = 0
    for i in range(len(h)):
        area = ((right_smaller[i]-left_smaller[i])+1) * h[i]
        if area > max_area:
            max_area = area
    print(max_area)

    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
