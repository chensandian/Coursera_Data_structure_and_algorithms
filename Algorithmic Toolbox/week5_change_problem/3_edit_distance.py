# Uses python3
def edit_distance(r, c):
    if r == 0 or c == 0 or matrix[r][c] != 0:
        return matrix[r][c]

    if row[r - 1] == col[c - 1]:
        matrix[r][c] = min(edit_distance(r - 1, c - 1),
                           edit_distance(r - 1, c) + 1,
                           edit_distance(r, c - 1) + 1)
    else:
        matrix[r][c] = min(edit_distance(r - 1, c - 1) + 1,
                           edit_distance(r - 1, c) + 1,
                           edit_distance(r, c - 1) + 1)
    return matrix[r][c]


if __name__ == "__main__":
    row = input()
    col = input()
    matrix = [[0 for col in range(len(col) + 1)] for row in range(len(row) + 1)]
    for r in range(len(row) + 1):
        matrix[r][0] = r
    for c in range(len(col) + 1):
        matrix[0][c] = c

    for r in range(1, len(row) + 1):
        for c in range(1, len(col) + 1):
            edit_distance(r, c)

    print(matrix[-1][-1])
