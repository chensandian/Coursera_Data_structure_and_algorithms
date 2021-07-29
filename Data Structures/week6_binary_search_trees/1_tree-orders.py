# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        stack = [0, 0]
        # every time we add a new node, we add it twice
        # one is for printing, the other for getting left child
        while stack:
            node_index = stack.pop()

            # if we haven't get its left child yet
            if stack and node_index == stack[-1]:
                if self.left[node_index] != -1:
                    stack.append(self.left[node_index])
                    stack.append(self.left[node_index])
            else:
                self.result.append(self.key[node_index])
                if self.right[node_index] != -1:
                    stack.append(self.right[node_index])
                    stack.append(self.right[node_index])
        return self.result

    def preOrder(self):
        self.result = []
        stack = [0]  # there is a least one node
        while stack:
            node_index = stack.pop()
            self.result.append(self.key[node_index])
            if self.right[node_index] != -1:
                stack.append(self.right[node_index])
            if self.left[node_index] != -1:
                stack.append(self.left[node_index])
        return self.result

    def postOrder(self):
        self.result = []
        stack = [0, 0]
        while stack:
            node_index = stack.pop()
            if stack and node_index == stack[-1]:
                if self.right[node_index] != -1:
                    stack.append(self.right[node_index])
                    stack.append(self.right[node_index])
                if self.left[node_index] != -1:
                    stack.append(self.left[node_index])
                    stack.append(self.left[node_index])
            else:
                self.result.append(self.key[node_index])
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
