from collections import Counter


def isAnagram(s, t):
    return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"
res = isAnagram(s, t)
print(res)
