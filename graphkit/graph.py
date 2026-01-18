from graphkit.algorithms.shortest_path.dijkstra import dijkstra
from graphkit.algorithms.shortest_path.bellman_ford import bellman_ford
from graphkit.algorithms.mst.kruskal import kruskal
from graphkit.algorithms.traversal.bfs import bfs
from graphkit.algorithms.traversal.dfs import dfs
from graphkit.algorithms.mst.prim import prim
from graphkit.algorithms.traversal.topological_sort import topological_sort

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
    
    def remove_edge(self, u, v, w=None):
        # Remove from adjacency list
        if u in self.adj:
            if w is None:
                self.adj[u] = [(x, wt) for x, wt in self.adj[u] if x != v]
            else:
                self.adj[u] = [(x, wt) for x, wt in self.adj[u] if not (x == v and wt == w)]

            if not self.adj[u]:
                del self.adj[u]

        if not self.directed and v in self.adj:
            if w is None:
                self.adj[v] = [(x, wt) for x, wt in self.adj[v] if x != u]
            else:
                self.adj[v] = [(x, wt) for x, wt in self.adj[v] if not (x == u and wt == w)]

            if not self.adj[v]:
                del self.adj[v]

        # Remove from edge list
        if w is None:
            self.edges = [(x, y, wt) for x, y, wt in self.edges if not (x == u and y == v)]
            if not self.directed:
                self.edges = [(x, y, wt) for x, y, wt in self.edges if not (x == v and y == u)]
        else:
            self.edges = [
                (x, y, wt)
                for x, y, wt in self.edges
                if not (x == u and y == v and wt == w)
            ]
            if not self.directed:
                self.edges = [
                    (x, y, wt)
                    for x, y, wt in self.edges
                    if not (x == v and y == u and wt == w)
                ]

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
    
    def prim(self, start):
        if self.directed:
            raise ValueError("Prim's algorithm requires an undirected graph")
        return prim(self.adj, start)
    
    def topological_sort(self):
        if not self.directed:
            raise ValueError("Topological sort requires a directed graph")
        return topological_sort(self.adj)
