x = 5
# a = int(x[2:].zfill(32), 10)
# print(a)
b = (x ^ 0xFFFFFFFF)
print(bin(b))
