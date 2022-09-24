import sys
nums = [1]
n = len(nums)
for i in range(n):
    for j in range(i+1, n+1):
        print(nums[i:j])

