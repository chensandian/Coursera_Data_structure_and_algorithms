# python3
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]


class Node:
    def __init__(self, i):
        self.r = 3 * i - 2
        self.g = 3 * i - 1
        self.b = 3 * i


clauses = []
# each vertex has to be colored by some color
for i in range(1, n + 1):
    node = Node(i)
    clauses.append([node.r, node.g, node.b])
    clauses.append([-node.r, -node.g])
    clauses.append([-node.r, -node.b])
    clauses.append([-node.g, -node.b])

for i, j in edges:
    u = Node(i)
    v = Node(j)
    # cannot have same color
    clauses.append([-u.r, -v.r])
    clauses.append([-u.g, -v.g])
    clauses.append([-u.b, -v.b])

print(len(clauses), n * 3)
for clause in clauses:
    for i in clause:
        print(i, end=" ")
    print(0)