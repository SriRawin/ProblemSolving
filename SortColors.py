def sortColors(nums):
    n = max(nums)
    curr = nums[:]
    count = [0]*(n+1)
    idx = [0]*(n+1)
    for i in curr:
        count[i] += 1
    for i in range(1, n+1):
        idx[i] = count[i-1]+idx[i-1]
    for i in range(len(curr)):
        nums[idx[curr[i]]] = curr[i]
        idx[curr[i]] += 1


nums = [1, 1]
res = sortColors(nums)
print(nums)
