def danceMoves(x, y):
    count = 0
    while y > x:
        x += 2
        count += 1
    while x > y:
        x -= 1
        count += 1
    print(count)


t = int(input())
for _ in range(t):
    case = list(map(int, input().split(" ")))
    danceMoves(case[0], case[1])
