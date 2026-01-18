import heapq

def prim(adj, start):
    visited = set()
    min_heap = [(0, start, None)]
    mst = []
    total_weight = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if u in visited:
            continue

        visited.add(u)
        if parent is not None:
            mst.append((parent, u, weight))
            total_weight += weight

        for v, w in adj.get(u, []):
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))

    return mst, total_weight
