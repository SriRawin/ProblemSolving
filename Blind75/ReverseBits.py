import re


def reverseBits(n):
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (32-i))
    return res


n = 3
res = reverseBits(n)
print(res)
