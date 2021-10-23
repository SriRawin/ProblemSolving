def minMaxLCM(x, k):
    y = x*k
    maxLCM = (y-1)*y
    minLCM = y
    for j in range(x+1, y+1):
        temp = j
        while(True):
            if (temp % x == 0) and (temp % j == 0):
                if temp < minLCM:
                    minLCM = temp
                break
            temp += 1
    print(minLCM, maxLCM)


t = int(input())
for _ in range(t):
    case = list(map(int, input().split(" ")))
    minMaxLCM(case[0], case[1])
