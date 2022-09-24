import math
import os
import random
import re
import sys


def freqQuery(queries):
    ds = {}
    ds_result = []
    for query, num in queries:
        if query == 1:
            ds[num] = ds.get(num, 0)+1
        if query == 2:
            if num in ds.keys():
                ds[num] = ds.get(num, 0)-1
        if query == 3:
            if num in ds.values():
                ds_result.append(1)
            else:
                ds_result.append(0)
    return ds_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
