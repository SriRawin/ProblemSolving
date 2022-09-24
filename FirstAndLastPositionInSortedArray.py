from ast import List


def searchRange(nums, target):
    if(len(nums)==0):
        return [-1,-1]
    start=0
    end =len(nums)-1
    i=0
    while(i<len(nums)):
        if(start>end):
            break
        if(nums[start]==target):
            pass
        else:
            start+=1
        if(nums[end]==target):
            pass
        else:
            end-=1
        i+=1
    if(end<start):
        return [-1,-1]
    else:
        return [start,end]


nums = [5,7,7,8,8,10] 
target = 8
result=searchRange(nums,target)
print(result)

