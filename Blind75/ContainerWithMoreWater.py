from email import header

# Brute-Force solution
# def maxArea(height):
#     area = 0
#     for l in range(1, 2):
#         for r in range(l+1, len(height)):
#             curr = (r-l)*min(height[l], height[r])
#             print(curr)
#             area = max(area, curr)
#     return area


def maxArea(height):
    l = 0
    r = len(height)-1
    area = 0
    while l < r:
        curr = (r-l)*min(height[l], height[r])
        area = max(area, curr)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        elif height[l] == height[r]:
            if height[l+1] < height[r-1]:
                l += 1
            else:
                r -= 1

    return area


height = [1, 1]
result = maxArea(height)
print(result)
