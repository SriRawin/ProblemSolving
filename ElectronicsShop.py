import os
import sys

#
# Complete the getMoneySpent function below.
#


def getMoneySpent(keyboards, drives, b):
    max = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            price = keyboards[i]+drives[j]
            max = price if (price > max and price <= b) else max
    print(max)
    return max if max > 0 else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
