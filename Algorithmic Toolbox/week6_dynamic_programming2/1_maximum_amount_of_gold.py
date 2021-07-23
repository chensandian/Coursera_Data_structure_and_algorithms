# Uses python3
import sys


def optimal_weight(W, w):

    matrix = [[0 for col in range(W + 1)] for row in range(n + 1)]
    for item in range(1, n + 1):
        for weight in range(1, W + 1):
            matrix[item][weight] = matrix[item - 1][weight]
            if w[item - 1] <= weight:
                value2 = matrix[item - 1][weight - w[item - 1]] + w[item - 1]
                if value2 > matrix[item][weight]:
                    matrix[item][weight] = value2
    return matrix[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
