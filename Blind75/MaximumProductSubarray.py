def maxProduct(nums):
    result = max(nums)
    max_product = 1
    min_product = 1
    for num in nums:
        if num == 0:
            max_product = min_product = 1
            continue
        curr = max_product*num
        max_product = max(num, curr, min_product*num)
        print("max", max_product)
        min_product = min(num, curr, min_product*num)
        print("min", min_product)
        result = max(result, max_product)
    return result


nums = [-1, -2, -3, -4]
result = maxProduct(nums)
print(result)
