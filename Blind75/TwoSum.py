def twoSum(nums, target: int):
    val_dict = {}
    for i in range(len(nums)):
        if val_dict.get(target-nums[i]) != None:
            return [val_dict.get(target-nums[i]), i]
        else:
            val_dict[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)
