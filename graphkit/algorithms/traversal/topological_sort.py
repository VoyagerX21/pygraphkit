from collections import deque, defaultdict

def topological_sort(adj):
    in_degree = defaultdict(int)
    nodes = set()

    # Collect nodes and compute in-degrees
    for u, neighbors in adj.items():
        nodes.add(u)
        for v, _ in neighbors:
            nodes.add(v)
            in_degree[v] += 1

    # Initialize queue with nodes having zero in-degree
    queue = deque([node for node in nodes if in_degree[node] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v, _ in adj.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != len(nodes):
        raise ValueError("Graph contains a cycle; topological sort not possible")

    return order
