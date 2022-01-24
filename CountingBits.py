def countBits(n):
    arr = [0]*(n+1)
    msb = 1
    for i in range(1, n+1):
        if msb*2 == i:
            msb = i
        arr[i] = 1+arr[i-msb]

    return arr


n = 5
res = countBits(n)
print(res)
