#Uses python3
import sys
import math


def minimum_distance(x, y):
    result = 0.
    connected = set()
    cost_list = [float('inf')] * n
    cost_list[0] = 0

    line = 0
    while line < n:
        min_cost = float('inf')
        curr_point = -1
        for index, cost in enumerate(cost_list):
            if cost < min_cost:
                min_cost = cost
                curr_point = index
        connected.add(curr_point)
        result += min_cost
        cost_list[curr_point] = float('inf')

        for i in range(n):
            d = math.sqrt((x[curr_point] - x[i]) ** 2 + (y[curr_point] - y[i]) ** 2)
            if i not in connected and d < cost_list[i]:
                cost_list[i] = d

        line += 1

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
