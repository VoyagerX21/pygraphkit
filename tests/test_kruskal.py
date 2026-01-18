from graphkit import Graph
import pytest


def test_kruskal_basic():
    g = Graph()
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(1, 3, 3)

    mst, total_weight = g.kruskal()

    assert total_weight == 3
    assert len(mst) == 2


def test_kruskal_single_edge():
    g = Graph()
    g.add_edge(1, 2, 10)

    mst, total_weight = g.kruskal()

    assert mst == [(1, 2, 10)]
    assert total_weight == 10


def test_kruskal_disconnected_graph():
    g = Graph()
    g.add_edge(1, 2, 1)
    g.add_edge(3, 4, 2)

    mst, total_weight = g.kruskal()

    # Forest, not a single tree
    assert total_weight == 3
    assert len(mst) == 2


def test_kruskal_directed_graph_error():
    g = Graph(directed=True)
    g.add_edge(1, 2, 1)

    with pytest.raises(ValueError):
        g.kruskal()
