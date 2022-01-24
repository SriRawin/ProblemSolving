from cv2 import randn


def missingNumber(nums):
    n = 0
    for idx, i in enumerate(nums, 1):
        n ^= idx
        n ^= i

    return n


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
res = missingNumber(nums)
print(res)
