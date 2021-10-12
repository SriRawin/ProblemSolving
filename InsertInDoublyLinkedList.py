import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(llist, data):
    node = DoublyLinkedListNode(data)
    current = llist
    while current:

        if current.prev == None:
            if data < current.data:
                current.prev = node
                node.next = current
                current = node
                return current

        if current.prev:
            if data >= current.prev.data and data <= current.data:
                current.prev.next = node
                node.next = current
                node.prev = current.prev
                return llist

        if current.next == None:
            if data >= current.data:
                current.next = node
                node.prev = current
                node.next = None
                return llist

        current = current.next

    return llist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
