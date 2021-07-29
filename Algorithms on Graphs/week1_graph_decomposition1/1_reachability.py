# Uses python3

import sys


def reach(adj, x, y):
    stack = [x]
    visited = set()
    visited.add(x)

    while stack:
        curr = stack.pop()
        for neighbor in adj[curr]:
            if neighbor in visited:
                continue
            if neighbor == y:
                return 1
            else:
                visited.add(neighbor)
                stack.append(neighbor)
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    num_vertices, num_edges = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * num_edges):2], data[1:(2 * num_edges):2]))
    x, y = data[2 * num_edges:]
    adj = [[] for _ in range(num_vertices)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
