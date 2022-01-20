def evenXOR(n):
    res = []
    c = 3
    while True and len(res) < n:
        curr = c
        count = 0
        while curr:
            curr &= (curr-1)
            count += 1
        if count % 2 == 0:
            res.append(c)
        c += 1

    print(*res)


tc = int(input())
for _ in range(tc):
    n = int(input())
    evenXOR(n)
