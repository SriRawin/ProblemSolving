# def weirdPalindrome(a):
#     shifts = 0
#     if len(a) == 1:
#         print(shifts)
#         return
#     if len(a) % 2 != 0:
#         i = 0
#         while i < len(a):
#             if a[i] % 2 != 0:
#                 for j in range(i+1, len(a)):
#                     if a[j] % 2 != 0:
#                         a[i] += a[j]
#                         del a[j]
#                         shifts += 1
#             i += 1
#     print(shifts)


t = int(input())
shifts = 0
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    print(a)
    for item in a:
        print(item)
        if item % 2 == 1:
            shifts += 1
    if shifts % 2 == 1:
        shifts -= 1
print(shifts//2)
