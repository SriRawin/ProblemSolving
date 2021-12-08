from collections import deque
import math
import os
import random
import re
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = Node(1)
        self.q = deque()
        self.q.append(self.root)
        self.node = None

    def insert(self, val):
        self.node = self.q.popleft()
        if val[0] == -1:
            pass
        else:
            self.node.left = Node(val[0])
            self.q.append(self.node.left)
        if val[1] == -1:
            pass
        else:
            self.node.right = Node(val[1])
            self.q.append(self.node.right)

    def traverse(self):
        q1 = deque()
        q1.append(self.root)
        result = []
        curr = q1.pop()
        while q1 or curr:
            if curr:
                q1.append(curr)
                curr = curr.left
            else:
                curr = q1.pop()
                result.append(curr.data)
                curr = curr.right
        return result

    def depth(self):
        depth = 0
        q = deque()
        q.append(self.root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth

    def swap(self, depth):
        curr_depth = 1
        q = deque()
        q.append(self.root)
        while q:
            if curr_depth == depth:
                for _ in range(len(q)):
                    node = q.popleft()
                    node.left, node.right = node.right, node.left

                return self.traverse()
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            curr_depth += 1


def swapNodes(indexes, queries):
    myTree = Tree()
    result = []
    swaps = []
    for v in indexes:
        myTree.insert(v)
    maxDepth = myTree.depth()
    for query in queries:
        temp = []
        temp.append(query)
        for i in range(query, maxDepth):
            if i*query < maxDepth and not i*query in temp:
                temp.append(i*query)
        swaps.append(temp)
    print(swaps)
    for swap in swaps:
        for i in swap:
            swapped = myTree.swap(i)
        result.append(swapped)

    print(result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
