def removeDuplicates(nums):
    k = len(nums)
    i = 0
    while i < len(nums):
        if i+1 < len(nums) and nums[i] == nums[i+1]:
            del nums[i]
            k -= 1
        else:
            i += 1
    return k


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = removeDuplicates(nums)
print(result)
