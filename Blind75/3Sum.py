

def threeSum(nums):
    res = []
    nums.sort()
    for idx, num in enumerate(nums):
        if idx > 0 and num == nums[idx-1]:
            continue
        l, r = idx+1, len(nums)-1
        while l < r:
            total = num+nums[l]+nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                res.append([num, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)
