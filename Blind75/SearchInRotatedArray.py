def search(nums, target):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if target > nums[mid] or target < nums[start]:
                start = mid+1
            else:
                end = mid-1
        else:
            if target < nums[mid] or target > nums[end]:
                end = mid-1
            else:
                start = mid+1

    return -1


nums = [6, 0, 1, 2, 3, 4]
target = 0

result = search(nums, target)
