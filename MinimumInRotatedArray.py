
def findMin(nums):
    res = nums[0]
    start = 0
    end = len(nums)-1
    if nums[0] <= nums[-1]:
        return nums[0]
    while start <= end:
        if nums[start] < nums[end]:
            return min(res,nums[start])
        mid = (start+end)//2
        res = min(res, nums[mid])
        
        if nums[mid] >= nums[start]:
            start = mid+1
        else:
            end = mid-1

    return start


nums = [4, 5, 6, 7, 0, 1, 2]
result = findMin(nums)
print(result)
