# python3
from collections import deque


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        #   Source: 1, Flights: 2, Crews: 3, Sink: 4
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m

        def bfs():
            visited = set()
            q = deque()
            q.append((1, None))
            visited.add((1, None))
            path = []
            parent = dict()

            while q:
                current = q.popleft()
                if current[0] == 1:
                    for i in range(n):
                        if matching[i] == -1:
                            visited.add((2, i))
                            parent[(2, i)] = (1, None)
                            q.append((2, i))

                elif current[0] == 2:
                    flight = current[1]
                    for crew in range(m):
                        if adj_matrix[flight][crew] == 1 and matching[flight] != crew and (3, crew) not in visited:
                            visited.add((3, crew))
                            parent[(3, crew)] = current
                            q.append((3, crew))

                elif current[0] == 3:
                    crew = current[1]
                    if not busy_right[crew]:
                        prev = current
                        current = (4, crew)
                        while True:
                            path.append((prev, current))
                            if prev[0] == 1:
                                break
                            current = prev
                            prev = parent[current]
                        for edge in path:
                            if edge[0][0] == 2:
                                matching[edge[0][1]] = edge[1][1]   # assign crew
                            elif edge[0][0] == 3 and edge[1][0] == 4:
                                busy_right[edge[1][1]] = True
                        return True
                    else:
                        for i in range(n):
                            if matching[i] == crew and (2, i) not in visited:
                                visited.add((2, i))
                                parent[(2, i)] = current
                                q.append((2, i))
            return False

        while bfs():
            continue
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
