nums = [-3, 2, -3, 4, 2]
startValue = 1
while startValue <= 10:
    total = startValue
    c=0
    print("start value", startValue)
    for num in nums:
        total += num
        if total >= 1:
            c+=1
    if c==len(nums):
        print("non-zero")

    startValue += 1
