nums = [-1, 0, 3,  5, 9, 12]
target = 12


def binarySearch(nums, target):
    if nums[len(nums)//2] == target:
        print(nums.index(target))
    elif target > nums[len(nums)//2]:
        return binarySearch(nums[(len(nums)//2)+1:], target)
    else:
        return binarySearch(nums[:len(nums)//2], target)


binarySearch(nums, target)
