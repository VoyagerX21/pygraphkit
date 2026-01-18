from graphkit import Graph
import pytest


def test_prim_basic():
    g = Graph()
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(1, 3, 3)

    mst, total_weight = g.prim(1)

    assert total_weight == 3
    assert len(mst) == 2


def test_prim_single_node():
    g = Graph()
    g.add_edge(1, 2, 5)

    mst, total_weight = g.prim(1)

    assert total_weight == 5
    assert mst == [(1, 2, 5)]


def test_prim_directed_error():
    g = Graph(directed=True)
    g.add_edge(1, 2, 1)

    with pytest.raises(ValueError):
        g.prim(1)
