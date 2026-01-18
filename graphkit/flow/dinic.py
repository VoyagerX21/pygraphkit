from collections import deque


class Edge:
    def __init__(self, v, cap):
        self.v = v
        self.cap = cap
        self.flow = 0
        self.rev = None


class FlowGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cap):
        if cap < 0:
            raise ValueError("Capacity must be non-negative")

        self.graph.setdefault(u, [])
        self.graph.setdefault(v, [])

        forward = Edge(v, cap)
        backward = Edge(u, 0)

        forward.rev = backward
        backward.rev = forward

        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def _bfs(self, s, t, level):
        for node in self.graph:
            level[node] = -1
        queue = deque([s])
        level[s] = 0

        while queue:
            u = queue.popleft()
            for e in self.graph[u]:
                if level[e.v] < 0 and e.flow < e.cap:
                    level[e.v] = level[u] + 1
                    queue.append(e.v)

        return level[t] >= 0

    def _dfs(self, u, t, f, level, it):
        if u == t:
            return f

        for i in range(it[u], len(self.graph[u])):
            it[u] = i
            e = self.graph[u][i]

            if e.cap > e.flow and level[e.v] == level[u] + 1:
                pushed = self._dfs(
                    e.v, t, min(f, e.cap - e.flow), level, it
                )
                if pushed:
                    e.flow += pushed
                    e.rev.flow -= pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        if s not in self.graph or t not in self.graph:
            raise ValueError("Source or sink not in graph")

        flow = 0
        level = {}
        INF = float("inf")

        while self._bfs(s, t, level):
            it = {u: 0 for u in self.graph}
            while True:
                pushed = self._dfs(s, t, INF, level, it)
                if not pushed:
                    break
                flow += pushed

        return flow

    def max_flow_with_min_cut(self, s, t):
        max_flow = self.max_flow(s, t)

        # Find reachable vertices from source in residual graph
        visited = set()
        stack = [s]

        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            for e in self.graph.get(u, []):
                if e.cap > e.flow and e.v not in visited:
                    stack.append(e.v)

        S = visited
        T = set(self.graph.keys()) - S

        return max_flow, (S, T)
