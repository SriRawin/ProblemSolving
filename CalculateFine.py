def calFine(returned, expected):
    fine = 0
    if returned[2] > expected[2]:
        fine += 10000
    elif returned[2] >= expected[2] and returned[1] > expected[1]:
        fine += (returned[1]-expected[1])*500
    elif returned[2] >= expected[2] and returned[1] >= expected[1] and returned[0] > expected[0]:
        fine += (returned[0]-expected[0])*15
    print(fine)


r_date = list(map(int, input().split(" ")))
e_date = list(map(int, input().split(" ")))
calFine(r_date, e_date)
