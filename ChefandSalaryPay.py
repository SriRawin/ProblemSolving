

def salary(pay, bonus, days):
    streak = 0
    max_streak = 0
    total_pay = 0
    print(days)
    for i in range(len(days)):
        if days[i] == '1':
            total_pay += pay
            streak += 1
        elif days[i] == '0':
            if streak > max_streak:
                max_streak = streak
            streak = 0
    if streak > max_streak:
        max_streak = streak
    bonus = bonus*max_streak
    total_pay += bonus
    print(total_pay)


n = int(input())
for _ in range(n):
    xy = list(map(int, input().split(" ")))
    p = str(input())
    salary(xy[0], xy[1], p)
