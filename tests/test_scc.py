from graphkit import Graph
import pytest


def test_scc_basic():
    g = Graph(directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    comps = g.strongly_connected_components()

    # Convert to sets for order independence
    comps = [set(c) for c in comps]

    assert set([0, 1, 2]) in comps
    assert set([3]) in comps


def test_scc_multiple_components():
    g = Graph(directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 2)

    comps = g.strongly_connected_components()
    comps = [set(c) for c in comps]

    assert set([0, 1]) in comps
    assert set([2, 3]) in comps


def test_scc_undirected_error():
    g = Graph()
    g.add_edge(1, 2)

    with pytest.raises(ValueError):
        g.strongly_connected_components()
