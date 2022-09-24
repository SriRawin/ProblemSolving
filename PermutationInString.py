from collections import Counter
s1 = "adc"
s2 = "dcda"
c = Counter(s1)
flag = False
n = len(s2)
m = len(s1)
for i in range(n):
    if c.get(s2[i]) and i+m <= n:
        curr = c.copy()
        count = 0
        print("main", curr)
        for j in range(i, i+m):
            if curr.get(s2[j]):
                curr[s2[j]] -= 1
                count += 1
                print(count, curr)
            else:
                break
        if count == m:
            flag = True
print(flag)
