from graphkit import Graph
import pytest


def test_floyd_warshall_basic():
    g = Graph(directed=True)
    g.add_edge(0, 1, 3)
    g.add_edge(1, 2, 4)
    g.add_edge(0, 2, 10)

    dist = g.floyd_warshall()

    assert dist[0][2] == 7
    assert dist[0][1] == 3


def test_floyd_warshall_negative_weights():
    g = Graph(directed=True)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -1)
    g.add_edge(0, 2, 4)

    dist = g.floyd_warshall()

    assert dist[0][2] == 0


def test_floyd_warshall_negative_cycle():
    g = Graph(directed=True)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -2)
    g.add_edge(2, 0, -2)

    with pytest.raises(ValueError):
        g.floyd_warshall()
