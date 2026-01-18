from graphkit.flow import FlowGraph


def test_min_cut_basic():
    g = FlowGraph()
    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 4)

    max_flow, (S, T) = g.max_flow_with_min_cut(0, 3)

    assert max_flow == 5
    assert 0 in S
    assert 3 in T
    assert S.isdisjoint(T)


def test_min_cut_simple_chain():
    g = FlowGraph()
    g.add_edge(0, 1, 5)
    g.add_edge(1, 2, 5)

    max_flow, (S, T) = g.max_flow_with_min_cut(0, 2)

    assert max_flow == 5
    assert S == {0}
    assert T == {1, 2}
