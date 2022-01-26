# def getSum(a, b):
#     m = 0xffffffff
#     while (b != 0):
#         c = a & b
#         a = (a ^ b) & m
#         b = (c << 1) & m
#     if (a >> 31) & 1:
#         return ~(a ^ m)
#     return a

def getSum(a, b):
    if b == 0:
        return a
    return getSum(a ^ b, (a & b) << 1)


a = -1
b = 1
result = getSum(a, b)
print(result)
