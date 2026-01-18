def bellman_ford(adj, edges, source):
    # Collect all nodes from edges
    nodes = set()
    for u, v, _ in edges:
        nodes.add(u)
        nodes.add(v)

    # Initialize distances
    dist = {node: float("inf") for node in nodes}
    dist[source] = 0

    # Relax edges |V|-1 times
    for _ in range(len(nodes) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            raise ValueError("Negative cycle detected")

    return dist
