from graphkit import Graph
import pytest


def test_topological_sort_basic():
    g = Graph(directed=True)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    order = g.topological_sort()

    # Validate ordering constraints
    assert order.index(5) < order.index(2)
    assert order.index(2) < order.index(3)
    assert order.index(3) < order.index(1)


def test_topological_sort_cycle():
    g = Graph(directed=True)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    with pytest.raises(ValueError):
        g.topological_sort()


def test_topological_sort_undirected_error():
    g = Graph()
    g.add_edge(1, 2)

    with pytest.raises(ValueError):
        g.topological_sort()
