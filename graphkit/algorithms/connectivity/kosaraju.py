from collections import defaultdict


def kosaraju(adj):
    visited = set()
    stack = []
    nodes = set()

    for u in adj:
        nodes.add(u)
        for v, _ in adj[u]:
            nodes.add(v)

    def dfs1(u):
        visited.add(u)
        for v, _ in adj.get(u, []):
            if v not in visited:
                dfs1(v)
        stack.append(u)

    for node in nodes:
        if node not in visited:
            dfs1(node)

    # Transpose graph
    transpose = defaultdict(list)
    for u in adj:
        for v, _ in adj[u]:
            transpose[v].append(u)

    visited.clear()
    components = []

    def dfs2(u, comp):
        visited.add(u)
        comp.append(u)
        for v in transpose.get(u, []):
            if v not in visited:
                dfs2(v, comp)

    while stack:
        node = stack.pop()
        if node not in visited:
            comp = []
            dfs2(node, comp)
            components.append(comp)

    return components
