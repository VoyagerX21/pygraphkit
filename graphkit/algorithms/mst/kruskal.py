from graphkit.utils.union_find import UnionFind

def kruskal(edges):
    uf = UnionFind()
    mst = []
    total_weight = 0

    edges = sorted(edges, key=lambda x: x[2])

    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight
