def isHappy(n: int):
    def square(num):
        return sum(int(n)**2 for n in str(num))
    tortoise = square(n)
    rabbit = square(square(n))
    while tortoise != rabbit and tortoise != 1:
        tortoise = square(tortoise)
        rabbit = square(square(rabbit))
    print(True if tortoise == 1 else False)


num = 19
isHappy(num)
