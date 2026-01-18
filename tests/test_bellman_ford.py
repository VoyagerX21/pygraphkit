from graphkit import Graph
import pytest


def test_bellman_ford_basic():
    g = Graph(directed=True)
    g.add_edge(0, 1, 5)
    g.add_edge(1, 2, 3)
    g.add_edge(0, 2, 10)

    dist = g.bellman_ford(0)

    assert dist[2] == 8


def test_bellman_ford_negative_weights():
    g = Graph(directed=True)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 2, -3)

    dist = g.bellman_ford(0)

    assert dist[2] == 1


def test_bellman_ford_negative_cycle():
    g = Graph(directed=True)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -1)
    g.add_edge(2, 0, -1)

    with pytest.raises(ValueError):
        g.bellman_ford(0)


def test_bellman_ford_unreachable_node():
    g = Graph(directed=True)
    g.add_edge(0, 1, 2)
    g.add_edge(2, 3, 1)

    dist = g.bellman_ford(0)

    assert dist[3] == float("inf")
