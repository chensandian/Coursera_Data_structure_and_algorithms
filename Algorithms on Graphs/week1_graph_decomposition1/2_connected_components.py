#Uses python3

import sys


def number_of_components(adj):
    result = 0
    visited = set()

    def reach_all(adj, x):
        if x in visited:
            return 0
        stack = [x]
        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if neighbor in visited:
                    continue
                else:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return 1

    for i in range(n):
        result += reach_all(adj, i)

    return result


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
    print(number_of_components(adj))
