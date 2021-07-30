#Uses python3

import sys
from collections import deque


def bipartite(adj):
    queue = deque()
    color_arr = [0 for _ in range(len(adj))]
    # use a for loop to check all node
    # in case the graph is separated into several components
    for i in range(len(adj)):
        if color_arr[i] == 0:
            queue.append(i)
            color_arr[i] = 1
            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if color_arr[neighbor] == 0:
                        color_arr[neighbor] = color_arr[curr] * -1
                        queue.append(neighbor)
                    elif color_arr[neighbor] == color_arr[curr]:
                        return 0

    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
