# Uses python3

import sys


def acyclic(adj):
    visited = [0 for _ in range(len(adj))]
    rec_stack = [0 for _ in range(len(adj))]
    for i in range(len(adj)):
        if not visited[i]:
            if dfs(adj, i, visited, rec_stack):
                return 1
    return 0

def dfs(adj, x, visited, rec_stack):
    # this will mark the points we traveled
    visited[x] = 1
    # this will mark the points we traveled but come back due to dead end
    # 1 marks we go pass; 0 marks we get back
    rec_stack[x] = 1
    for neighbor in adj[x]:
        if visited[neighbor] == 0 and dfs(adj, neighbor, visited, rec_stack):
            return 1
        elif rec_stack[neighbor] == 1:
            return 1
    # if we get to this part, that means we reached a dead end
    rec_stack[x] = 0
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
