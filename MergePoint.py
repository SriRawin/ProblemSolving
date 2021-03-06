
import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def length_linkedList(llist):
    count = 0
    
    while llist:
        count += 1
        llist = llist.next
    return count


def findMergeNode(head1, head2):
    len_head1 = length_linkedList(head1)
    len_head2 = length_linkedList(head2)
    if (len_head1 > len_head2):
        i = len_head1-len_head2
        for _ in range(i):
            head1 = head1.next
    if (len_head2 > len_head1):
        i = len_head2-len_head1
        for _ in range(i):
            head2 = head2.next
    if (len_head1 == len_head2):
        head1 = head1.next
        head2 = head2.next

    while head1:

        if head1 == head2:

            return head1.data
        head1 = head1.next
        head2 = head2.next


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next

        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()
