from collections import Counter


def firstUnique():
    s = "aabb"
    c = Counter(s)
    for i in range(len(s)):
        if c[s[i]] == 1:
            print(i)
            return

    return -1


firstUnique()
