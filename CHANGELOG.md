# Changelog

All notable changes to **graphkit** are documented in this file.

This project follows **Semantic Versioning**.

---

## [0.7.0] - 2026-01-18

### Added
- `FlowGraph` abstraction for flow networks
- Dinic’s algorithm for maximum flow
- Residual graph handling
- Test coverage for max flow

---

## [0.6.0] - 2026-01-18

### Added
- Strongly Connected Components using Kosaraju’s algorithm
- `Graph.strongly_connected_components()` API
- Test coverage for SCC detection

---

## [0.5.0] - 2026-01-18

### Added
- Floyd–Warshall algorithm for all-pairs shortest paths
- `Graph.floyd_warshall()` API
- Negative cycle detection
- Comprehensive test coverage

---

## [0.4.0] - 2026-01-18

### Added
- Topological Sort for directed acyclic graphs (DAGs)
- `Graph.topological_sort()` API
- Cycle detection with `ValueError`
- Test coverage for valid DAGs and cycles

---

## [0.3.0] – 2026-01-18

### Added

* Prim’s Algorithm for Minimum Spanning Tree
* `Graph.prim(start)` API for undirected graphs
* Priority-queue based greedy MST implementation
* Test coverage for Prim’s algorithm

---

## [0.2.0] – 2026-01-18

### Added

* `remove_edge` method to `Graph` class
* Support for edge removal in directed and undirected graphs
* Optional weight-specific edge removal
* Test coverage for edge removal behavior

---

## [0.1.1] – 2026-01-18

### Fixed

* Corrected Bellman–Ford implementation to include destination-only vertices
* Fixed `KeyError` issues for unreachable nodes
* Improved negative weight handling
* Added early-exit optimization to Bellman–Ford

### Added

* Comprehensive test coverage for:

  * Bellman–Ford algorithm
  * Kruskal’s algorithm
* Edge-case testing for disconnected graphs
* Negative cycle detection tests

---

## [0.1.0] – Initial Release

### Added

* Graph abstraction (directed and undirected)
* Dijkstra’s algorithm
* Bellman–Ford algorithm
* Kruskal’s algorithm
* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Initial test suite
