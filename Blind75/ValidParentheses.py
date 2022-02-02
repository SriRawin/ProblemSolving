import re


def isValid(s):
    stack = []
    parantheses = {"(": ")", "{": "}", "[": "]"}
    for c in s:
        if not stack:
            stack.append(c)
        elif c == parantheses.get(stack[-1]):
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return False
    return True


s = "({[]})"
res = isValid(s)
print(res)
