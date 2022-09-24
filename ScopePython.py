
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        temp = 0
        for i in range(len(self.__elements)-1):
            for j in range(i+1, len(self.__elements)):
                temp = abs(self.__elements[i]-self.__elements[j])
                if temp > self.maximumDifference:
                    self.maximumDifference = temp


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
