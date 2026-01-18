# graphkit

![PyPI](https://img.shields.io/pypi/v/pygraphkit)
![Python](https://img.shields.io/pypi/pyversions/pygraphkit)
![Tests](https://github.com/VoyagerX21/graphkit/actions/workflows/tests.yml/badge.svg)

**graphkit** is a clean, reusable Python library providing standard graph algorithms with a unified and intuitive API.

It is designed for:

* Learning and revision of graph algorithms
* Interview and competitive programming preparation
* Real-world projects requiring graph processing
* Avoiding repeated reimplementation of well-known algorithms

---

## ✨ Features

* Simple `Graph` abstraction
* Object-oriented API
* Readable and canonical implementations
* Fully tested with CI
* No external runtime dependencies

### Algorithms included

**Shortest Path**

* Dijkstra’s Algorithm
* Bellman–Ford Algorithm

**Minimum Spanning Tree**

* Kruskal’s Algorithm
* Prim’s Algorithm

**Traversals**

* Breadth-First Search (BFS)
* Depth-First Search (DFS)

---

## 📦 Installation

```bash
pip install pygraphkit
```

For development:

```bash
pip install -e .
```

---

## 🚀 Quick Start

```python
from graphkit import Graph

g = Graph()
g.add_edge(1, 2, 4)
g.add_edge(1, 3, 1)
g.add_edge(3, 2, 2)

print(g.dijkstra(1))
```

**Output**

```text
{1: 0, 2: 3, 3: 1}
```

---

## 🧠 Core Concept

### Graph Abstraction

All algorithms operate on a single `Graph` class.

```python
Graph(directed=False)
```

* `directed=False` → undirected graph
* `directed=True` → directed graph

---

### Adding edges

```python
g.add_edge(u, v, weight)
```

* Default weight is `1`
* For undirected graphs, edges are added both ways

---

### Removing edges

Edges can be removed dynamically using `remove_edge`.

```python
g.remove_edge(u, v)
```

#### Remove a specific weighted edge

```python
g.remove_edge(u, v, weight)
```

**Behavior**

* For **undirected graphs**, both directions are removed
* For **directed graphs**, only `u → v` is removed
* If the edge does not exist, the operation is a no-op

---

## 📐 API Reference

### Dijkstra’s Algorithm

Finds shortest paths from a source node (non-negative weights).

```python
g.dijkstra(source)
```

Returns:

```python
{node: shortest_distance}
```

---

### Bellman–Ford Algorithm

Supports negative edge weights and detects negative cycles.

```python
g.bellman_ford(source)
```

Raises:

```text
ValueError: Negative cycle detected
```

---

### Kruskal’s Algorithm

Computes the Minimum Spanning Tree (undirected graphs only).

```python
mst, total_weight = g.kruskal()
```

Returns:

* `mst`: list of edges `(u, v, w)`
* `total_weight`: sum of MST edge weights

---

### Prim’s Algorithm

Computes the Minimum Spanning Tree starting from a given node.

```python
mst, total_weight = g.prim(start)
```

* Works on **undirected graphs**
* Uses a greedy priority-queue approach

---

### Breadth-First Search (BFS)

```python
g.bfs(source)
```

Returns traversal order as a list.

---

### Depth-First Search (DFS)

```python
g.dfs(source)
```

Returns traversal order as a list.

---

## 🧪 Testing

`graphkit` uses **pytest** for testing all core algorithms.

The test suite covers:

* Shortest path correctness
* Negative edge weights
* Negative cycle detection
* Disconnected graphs
* Error handling for invalid usage

Run tests locally:

```bash
pip install -e .
pytest -v
```

All tests must pass before a release is published.

---

## 📁 Project Structure

```
graphkit/
├── graphkit/
│   ├── graph.py
│   ├── algorithms/
│   ├── utils/
│   └── __init__.py
│
├── tests/
│   └── test_*.py
│
├── README.md
├── pyproject.toml
└── LICENSE
```

---

## 🎯 Design Philosophy

* One **canonical implementation** per algorithm
* Code clarity over cleverness
* No premature optimization
* Easy to rewrite during competitive programming
* Reusable in real-world systems

---

## 🛣️ Roadmap

Planned additions:

* Floyd–Warshall Algorithm
* Topological Sort
* Strongly Connected Components (Kosaraju / Tarjan)
* Maximum Flow algorithms (Edmonds–Karp, Dinic)
* Benchmarking utilities

---

## 🤝 Contributing

Contributions are welcome.

You can help by:

* Adding algorithms
* Improving test coverage
* Enhancing documentation

Please keep implementations:

* Clean
* Readable
* Well-tested

---

## 📜 License

MIT License
