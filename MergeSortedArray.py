nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
# [1,2,3,2,5,6]
m = 3
n = len(nums2)
for _ in range(len(nums1)-m):
    nums1.pop()
for i in range(n):
    nums1.append(nums2[i])
print(nums1)
for i in range(m, m + n):
    print(m)
    key = nums1[i]
    print(key)
    j = abs(i-1)
    while j >= 0 and key < nums1[j]:
        nums1[j+1] = nums1[j]
        j -= 1
    nums1[j+1] = key
print(nums1)
