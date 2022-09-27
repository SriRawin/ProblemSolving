import re


def backspaceCompare(s, t) -> bool:
    s = removeBackspace(s)
    t = removeBackspace(t)
    return s == t


def removeBackspace(text):
    res = ""
    for char in text:
        if(char != "#"):
            res += char
        else:
            res = res[:-1]
    return res


s = "ab#c"
t = "ad#c"
res = backspaceCompare(s, t)
print(res)
