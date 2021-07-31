#Uses python3

import sys


def negative_cycle(adj, cost):
    dist = [float('inf')] * len(adj)
    dist[0] = 0
    for i in range(len(adj)):
        for u in range(len(adj)):
            for index, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][index]:
                    dist[v] = dist[u] + cost[u][index]
                    if i == len(adj) - 1:
                        return 1
        # if the graph is separated into several components, need to initial dist 0 again
        for point in range(i + 1, len(adj)):
            if dist[point] == float('inf'):
                dist[point] = 0
                break
    return 0


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
    print(negative_cycle(adj, cost))
