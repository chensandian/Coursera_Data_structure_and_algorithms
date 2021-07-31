#Uses python3

import sys
from collections import deque


def distance(adj, cost, s, t):
    queue = deque()
    queue.append(s)
    total_cost = [float('inf')] * len(adj)
    total_cost[s] = 0
    visited = set()
    visited.add(s)

    while queue:
        curr = queue.popleft()
        for index in range(len(adj[curr])):
            if adj[curr][index] not in visited:
                queue.append(adj[curr][index])
                visited.add(adj[curr][index])
            if total_cost[adj[curr][index]] > total_cost[curr] + cost[curr][index]:
                total_cost[adj[curr][index]] = total_cost[curr] + cost[curr][index]

    return total_cost[t] if t in visited else -1


def distance2(adj, cost, s, t):
    next_nodes = set()
    next_nodes.add(s)
    total_cost = [float('inf')] * len(adj)
    total_cost[s] = 0
    visited = set()
    visited.add(s)

    while next_nodes:
        small = float('inf')
        small_node = 0
        for index in next_nodes:
            if small > total_cost[index]:
                small = total_cost[index]
                small_node = index
        next_nodes.remove(small_node)

        curr = small_node
        for index in range(len(adj[curr])):
            if adj[curr][index] not in visited:
                next_nodes.add(adj[curr][index])
                visited.add(adj[curr][index])
            if total_cost[adj[curr][index]] > total_cost[curr] + cost[curr][index]:
                total_cost[adj[curr][index]] = total_cost[curr] + cost[curr][index]

    return total_cost[t] if t in visited else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance2(adj, cost, s, t))
