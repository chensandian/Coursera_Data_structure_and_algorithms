# python3
from collections import deque


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        # in the order of forward/backward forward/backward ...
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        # get all the possible edges (#ids) from one city
        return self.graph[from_]

    def get_edge(self, id):
        # return an Edge object with from/to/capacity information
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        # even id will get id + 1; odd id will get id - 1
        # adding flow to one direction means decreasing in the opposite direction
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity += flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def bfs(graph, from_, to):
    have_path = False
    path = []
    neck = 10001
    distance = [float("inf")] * graph.size()
    parent = [(None, None)] * graph.size()

    queue = deque()
    distance[from_] = 0
    queue.append(from_)

    while queue:
        curr_from_node = queue.popleft()
        for id in graph.get_ids(curr_from_node):
            curr_edge = graph.get_edge(id)
            if distance[curr_edge.v] == float("inf") and curr_edge.capacity > 0:
                distance[curr_edge.v] = distance[curr_from_node] + 1
                parent[curr_edge.v] = (curr_from_node, id)
                queue.append(curr_edge.v)
                if curr_edge.v == to:
                    while True:
                        path.append(id)
                        neck = min(neck, graph.get_edge(id).capacity)
                        if curr_from_node == from_:
                            break
                        curr_from_node, id = parent[curr_from_node]
                    have_path = True
                    return have_path, path, neck

    return have_path, path, neck


def max_flow(graph, from_, to):
    flow = 0
    while True:
        have_path, path, neck = bfs(graph, from_, to)
        if not have_path:
            return flow
        for id in path:
            graph.add_flow(id, neck)
        flow += neck


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
