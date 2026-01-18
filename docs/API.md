# graphkit Public API (Stable)

This document describes the **stable public API** of graphkit.
Breaking changes will only occur in major versions.

---

## Graph

```python
Graph(directed: bool = False)
```

### Methods

* `add_edge(u, v, weight=1)`
* `remove_edge(u, v, weight=None)`
* `dijkstra(source)`
* `bellman_ford(source)`
* `floyd_warshall()`
* `kruskal()`
* `prim(start)`
* `bfs(source)`
* `dfs(source)`
* `topological_sort()`
* `strongly_connected_components()`

---

## FlowGraph

```python
FlowGraph()
```

### Methods

* `add_edge(u, v, capacity)`
* `max_flow(source, sink)`
* `max_flow_with_min_cut(source, sink)`

---

## Exceptions

Algorithms raise `ValueError` for:

* invalid graph type (directed vs undirected)
* negative cycles
* cyclic DAG operations
* invalid source or sink nodes
