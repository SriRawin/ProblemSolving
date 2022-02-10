def countSubstrings(s):
    n = len(s)
    count=0
    for i in range(n):
        for j in range(2):
            l, r = i, i+j
            while l >= 0 and r < n and s[l] == s[r]:
                count+=1
                l -= 1
                r += 1
    return count


s = "aaa"
res = countSubstrings(s)
print(res)
