def productExceptSelf(nums):
    n = len(nums)
    answers = [1]*n
    prev = 1
    for i in range(n):
        answers[i] *= prev
        prev *= nums[i]
    prev = 1
    for i in range(n-1, -1, -1):
        answers[i] *= prev
        prev *= nums[i]

    return answers


nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)
