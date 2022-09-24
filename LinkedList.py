from email import header


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            self.curr = self.head
        else:
            self.curr.next = Node(data)
            self.curr = self.curr.next

    def insertBylist(self, customList):
        for data in customList:
            if not self.head:
                self.head = Node(data)
                self.curr = self.head
            else:
                self.curr.next = Node(data)
                self.curr = self.curr.next

    def display(self):
        temp = self.head
        while True:
            if not temp:
                print(None)
                break
            print(temp.data, end=" -> "),
            temp = temp.next


mylist = LinkedList()
# mylist.insert(2)
# mylist.insert(4)
# mylist.insert(6)
# mylist.insert(8)
# mylist.insert(10)
mylist.display()
ls = [1, 3, 5, 7, 8, 9]
mylist.insertBylist(ls)
mylist.display()
