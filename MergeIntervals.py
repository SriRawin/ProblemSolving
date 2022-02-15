

def merge(intervals):
    intervals.sort()
    l = 0
    r = l+1
    res = []
    curr = []
    while l < len(intervals):
        if not curr:
            curr = intervals[l]
        if r >= len(intervals):
            res.append(curr)
            return res

        if curr[1] >= intervals[r][0]:
            curr[1] = max(curr[1], intervals[r][1])
            r += 1
        else:
            res.append(curr)
            curr = []
            l = r
            r = l+1
    return res


intervals = [[1, 4], [0, 4]]
res = merge(intervals)
print(res)
