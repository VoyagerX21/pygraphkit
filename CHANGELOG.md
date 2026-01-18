# Changelog

All notable changes to **graphkit** are documented in this file.

This project follows **Semantic Versioning**.

---

## [0.1.1] – 2026-01-18

### Fixed

* Corrected Bellman-Ford implementation to include destination-only vertices
* Fixed KeyError issues for unreachable nodes
* Improved negative weight handling
* Added early-exit optimization to Bellman-Ford

### Added

* Comprehensive test coverage for:

  * Bellman-Ford
  * Kruskal’s algorithm
* Edge case testing for disconnected graphs
* Negative cycle detection tests

---

## [0.1.0] – Initial Release

### Added

* Graph abstraction (directed and undirected)
* Dijkstra’s algorithm
* Bellman-Ford algorithm
* Kruskal’s algorithm
* BFS and DFS traversals
* Initial test suite
