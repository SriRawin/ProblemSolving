from collections import defaultdict


def groupAnagrams(strs):
    grp = defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)-ord("a")] += 1
        grp[tuple(count)].append(s)
        print(grp)
    return list(grp.values())


sts = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(sts)
print(res)
