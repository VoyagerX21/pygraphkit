def floyd_warshall(adj):
    # Collect all nodes
    nodes = set(adj.keys())
    for u in adj:
        for v, _ in adj[u]:
            nodes.add(v)

    # Initialize distance matrix
    dist = {
        u: {v: float("inf") for v in nodes}
        for u in nodes
    }

    for u in nodes:
        dist[u][u] = 0

    for u in adj:
        for v, w in adj[u]:
            dist[u][v] = min(dist[u][v], w)

    # Floyd–Warshall core
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Detect negative cycles
    for node in nodes:
        if dist[node][node] < 0:
            raise ValueError("Graph contains a negative cycle")

    return dist
