from collections import deque


def dailyTemperature():
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    answer = [0]*len(temperatures)
    stack = deque()
    for i, cur in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < cur:
            print(temperatures[stack[-1]])
            prev_i = stack.pop()
            answer[prev_i] = i - prev_i
        stack.append(i)
    print(answer)


dailyTemperature()
