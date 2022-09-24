def examResult(n, x, p):
    print(n, x, p)
    marks = x*3
    wrong = n-x
    negative_marks = 1*wrong
    print(negative_marks)
    marks -= negative_marks
    print(marks)
    if marks >= p:
        print("PASS")
    else:
        print("FAIL")


n = int(input())
for _ in range(n):
    x = list(map(int, input().split(" ")))
    examResult(x[0], x[1], x[2])
