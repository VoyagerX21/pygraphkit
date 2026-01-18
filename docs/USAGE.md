# Using graphkit from the Python CLI

This guide shows how to use **graphkit** interactively from the command line
(using the Python REPL) or inside scripts.

Install first:

```bash
pip install pygraphkit
```

Start Python:

```bash
python
```

---

## 1. Working with Graphs

Import the core graph abstraction:

```python
from graphkit import Graph
```

### Undirected graph (default)

```python
g = Graph()
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 1)
```

### Directed graph

```python
g = Graph(directed=True)
g.add_edge("A", "B", 5)
```

---

## 2. Shortest Path Algorithms

### Dijkstra (non-negative weights)

```python
dist = g.dijkstra(source)
```

Example:

```python
g = Graph()
g.add_edge(1, 2, 4)
g.add_edge(1, 3, 1)
g.add_edge(3, 2, 2)

print(g.dijkstra(1))
```

Output:

```text
{1: 0, 2: 3, 3: 1}
```

---

### Bellman–Ford (negative weights allowed)

```python
dist = g.bellman_ford(source)
```

If a negative cycle exists:

```text
ValueError: Negative cycle detected
```

---

### Floyd–Warshall (all-pairs shortest paths)

```python
dist = g.floyd_warshall()
```

Access distances:

```python
dist[u][v]
```

---

## 3. Minimum Spanning Tree (Undirected Graphs)

### Kruskal’s Algorithm

```python
mst, total_weight = g.kruskal()
```

---

### Prim’s Algorithm

```python
mst, total_weight = g.prim(start_node)
```

---

## 4. Graph Traversals

### Breadth-First Search (BFS)

```python
order = g.bfs(source)
```

---

### Depth-First Search (DFS)

```python
order = g.dfs(source)
```

---

## 5. Directed Acyclic Graphs (DAG)

### Topological Sort

```python
order = g.topological_sort()
```

If the graph contains a cycle:

```text
ValueError: Graph contains a cycle
```

---

## 6. Strongly Connected Components

```python
components = g.strongly_connected_components()
```

Each component is returned as a list of nodes.

---

## 7. Flow Networks (Max-Flow / Min-Cut)

Flow algorithms use a **separate abstraction**.

```python
from graphkit.flow import FlowGraph
```

### Maximum Flow (Dinic)

```python
g = FlowGraph()
g.add_edge(0, 1, 3)
g.add_edge(1, 2, 2)

max_flow = g.max_flow(0, 2)
```

---

### Minimum Cut

```python
max_flow, (S, T) = g.max_flow_with_min_cut(0, 2)
```

* `S`: vertices reachable from source in residual graph
* `T`: remaining vertices

---

## Notes

* Nodes can be any hashable type (int, str, tuple, etc.)
* Algorithms raise `ValueError` on invalid usage
* The public API is stable starting from **v1.0.0**
