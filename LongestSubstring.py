from collections import deque
s = "tmmzuxt"
q = deque()
longest = 0
curr = 0
str_dict = {}
n = len(s)
i = 0
while i < n:
    if str_dict.get(s[i]) == None:
        str_dict.update({s[i]: 1})
        q.append(s[i])
        curr += 1
        print(q, str_dict)
    elif str_dict.get(s[i]) != None:
        while q:
            curr -= 1
            str_dict.pop(q[0])
            if q[0] == s[i]:
                q.popleft()
                break
            elif q[0] != s[i]:
                q.popleft()
        str_dict.update({s[i]: 1})
        q.append(s[i])
        curr += 1
        print(q, str_dict)

    longest = max(longest, curr)
    print("curr", curr, "longest", longest)

    i += 1
print(longest)
