def maxSubArray(nums):
    curr = 0
    max_ss = nums[0]
    for n in nums:
        if curr < 0:
            curr = 0
        curr += n
        max_ss = max(curr, max_ss)
    return max_ss


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = maxSubArray(nums)
print(res)
