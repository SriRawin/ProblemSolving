from collections import Counter


def minWindow(s, t):
    if t == "":
        return ""
    t_dict = Counter(t)
    l = 0
    res = [l, l]
    resLen = float("infinity")
    s_dict = {}
    need = len(t)
    have = 0
    for r in range(len(s)):
        s_dict[s[r]] = 1+s_dict.get(s[r], 0)
        if t_dict.get(s[r]) and t_dict[s[r]] >= s_dict[s[r]]:
            have += 1
        while need == have:
            if (r-l+1) < resLen:
                res = [l, r]
                resLen = r-l+1
            s_dict[s[l]] -= 1
            if t_dict.get(s[l]) and s_dict[s[l]] < t_dict[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if resLen != float("infinity") else ""


s = "aa"
t = "aa"
res = minWindow(s, t)
print(res)
