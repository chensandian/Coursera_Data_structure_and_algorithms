#Uses python3

import sys


def lcs2(a, b):
    matrix = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                matrix[j][i] = matrix[j - 1][i - 1] + 1
            else:
                matrix[j][i] = max(matrix[j - 1][i], matrix[j][i - 1])
    return matrix[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    list1 = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    list2 = data[:m]

    print(lcs2(list1, list2))