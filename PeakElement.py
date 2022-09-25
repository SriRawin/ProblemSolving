def findPeakElement( nums):
    peak=0
    i=1
    while(i<len(nums)):
        if(nums[peak]>nums[i]):
            return peak
        else:
            peak+=1
        i+=1
    return peak



nums = [1,2,3,1]
res=findPeakElement(nums)
print(res)