from graphkit.algorithms.shortest_path.dijkstra import dijkstra
from graphkit.algorithms.shortest_path.bellman_ford import bellman_ford
from graphkit.algorithms.mst.kruskal import kruskal
from graphkit.algorithms.traversal.bfs import bfs
from graphkit.algorithms.traversal.dfs import dfs


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}
        self.edges = []

    def add_edge(self, u, v, w=1):
        self.adj.setdefault(u, []).append((v, w))
        if not self.directed:
            self.adj.setdefault(v, []).append((u, w))

        self.edges.append((u, v, w))

    def dijkstra(self, source):
        return dijkstra(self.adj, source)

    def bellman_ford(self, source):
        return bellman_ford(self.adj, self.edges, source)

    def kruskal(self):
        if self.directed:
            raise ValueError("Kruskal requires an undirected graph")
        return kruskal(self.edges)

    def bfs(self, source):
        return bfs(self.adj, source)

    def dfs(self, source):
        return dfs(self.adj, source)
