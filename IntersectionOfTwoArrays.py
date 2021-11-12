nums1 = [1, 1]
nums2 = [1, 2]
n = len(nums1)
m = len(nums2)
intersect = []
if n > m:
    smaller = nums2
    bigger = nums1
else:
    smaller = nums1
    bigger = nums2
for i in smaller:
    for j in range(len(bigger)):
        if i == bigger[j]:
            intersect.append(i)
            del bigger[j]
            break

print(intersect)

