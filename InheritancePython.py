class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        marks_list = self.scores
        total = 0
        for i in range(len(marks_list)):
            total += marks_list[i]
        marks = total//len(marks_list)
        print(total)
        print(marks)
        if marks >= 90 and marks <= 100:
            return "O"
        elif marks >= 80 and marks < 90:
            return "A"
        elif marks >= 70 and marks < 80:
            return "P"
        elif marks >= 55 and marks < 70:
            return "D"
        elif marks >= 40 and marks < 55:
            return "T"
        elif marks < 40:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
