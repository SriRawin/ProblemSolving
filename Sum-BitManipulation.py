def getSum(a, b):
    m = 0xffffffff
    while (b != 0):
        c = a & b
        a = (a ^ b) & m
        b = (c << 1) & m
    if (a >> 31) & 1:
        return ~(a ^ m)
    return a


a = -1
b = 0
result = getSum(a, b)
print(result)
