from collections import deque

def bfs(adj, source):
    visited = set()
    order = []

    q = deque([source])
    visited.add(source)

    while q:
        u = q.popleft()
        order.append(u)

        for v, _ in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)

    return order
