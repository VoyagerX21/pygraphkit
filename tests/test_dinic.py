from graphkit.flow import FlowGraph


def test_dinic_basic():
    g = FlowGraph()
    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 4)

    assert g.max_flow(0, 3) == 5


def test_dinic_single_path():
    g = FlowGraph()
    g.add_edge(0, 1, 10)
    g.add_edge(1, 2, 5)

    assert g.max_flow(0, 2) == 5


def test_dinic_disconnected():
    g = FlowGraph()
    g.add_edge(0, 1, 3)
    g.add_edge(2, 3, 4)

    assert g.max_flow(0, 3) == 0
