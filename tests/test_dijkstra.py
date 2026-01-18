from graphkit import Graph

def test_dijkstra():
    g = Graph()
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 1)
    g.add_edge(3, 2, 2)

    dist = g.dijkstra(1)
    assert dist[2] == 3
