"""CSC 225 - Construct the test graphs and display search orders."""
from graph import Graph


def make_graph_1():
    g = Graph()
    for u, v in [('A', 'B'), ('A', 'C'), ('B', 'D'),
                 ('B', 'E'), ('C', 'F'), ('E', 'F')]:
        g.add_edge(u, v)
    return g


def make_graph_2():
    g = Graph()
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 3)]:
        g.add_edge(u, v)
    return g


def make_graph_3():
    g = Graph()
    for u, v in [('A', 'B'), ('B', 'C'), ('X', 'Y')]:
        g.add_edge(u, v)
    g.add_vertex('Z')
    return g


if __name__ == '__main__':
    for label, g, start in [
        ('Graph 1', make_graph_1(), 'A'),
        ('Graph 2', make_graph_2(), 0),
        ('Graph 3', make_graph_3(), 'A'),
        ('Isolated vertex', make_graph_3(), 'Z'),
    ]:
        print('\n' + label)
        print('Adjacency list:', g.adj)
        print('DFS:', g.dfs(start))
        print('BFS:', g.bfs(start))
