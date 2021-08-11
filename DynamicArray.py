import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    result_list=[[] for _ in range(n)]
    answer_list=[]
    last_answer=0
    for case,x,y in queries:
        if case==1:
            result_list[(x^last_answer)%n].append(y)
        else:
            last_answer=result_list[(x^last_answer)%n][y%len(result_list[(x^last_answer)%n])]
            answer_list.append(last_answer)

    return answer_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
