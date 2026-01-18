def dfs(adj, source):
    visited = set()
    order = []

    def _dfs(u):
        visited.add(u)
        order.append(u)

        for v, _ in adj[u]:
            if v not in visited:
                _dfs(v)

    _dfs(source)
    return order
