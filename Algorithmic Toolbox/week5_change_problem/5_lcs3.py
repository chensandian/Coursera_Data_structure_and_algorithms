#Uses python3

import sys


def lcs3(a, b, c):
    matrix = [[[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)] for k in range(len(c) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    matrix[k][j][i] = matrix[k - 1][j - 1][i - 1] + 1
                else:
                    matrix[k][j][i] = max(matrix[k - 1][j][i], matrix[k][j - 1][i], matrix[k][j][i - 1])

    return matrix[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
