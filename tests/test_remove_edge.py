from graphkit import Graph


def test_remove_edge_undirected():
    g = Graph()
    g.add_edge(1, 2, 3)

    g.remove_edge(1, 2)

    assert 1 not in g.adj
    assert 2 not in g.adj
    assert g.edges == []


def test_remove_edge_directed():
    g = Graph(directed=True)
    g.add_edge(1, 2, 3)

    g.remove_edge(1, 2)

    assert 1 not in g.adj
    assert g.edges == []


def test_remove_edge_with_weight():
    g = Graph()
    g.add_edge(1, 2, 3)
    g.add_edge(1, 2, 5)

    g.remove_edge(1, 2, 3)

    assert (1, 2, 5) in g.edges
    assert (1, 2, 3) not in g.edges
