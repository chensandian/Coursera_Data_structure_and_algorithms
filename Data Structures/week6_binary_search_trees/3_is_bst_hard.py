#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    curr_max = float("-inf")
    prev_node_index = -2
    # inOrder traversal, make sure the next value is > than curr_max

    if len(tree) <= 1:
        return True
    else:
        stack = [0, 0]

    while stack:
        node_index = stack.pop()
        if stack and node_index == stack[-1]:
            if tree[node_index][1] != -1:
                stack.append(tree[node_index][1])
                stack.append(tree[node_index][1])
        else:
            if tree[node_index][0] < curr_max:
                return False
            elif tree[node_index][0] == curr_max and tree[node_index][1] == prev_node_index:
                return False
            else:
                curr_max = tree[node_index][0]

            if tree[node_index][2] != -1:
                stack.append(tree[node_index][2])
                stack.append(tree[node_index][2])
            prev_node_index = node_index
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
