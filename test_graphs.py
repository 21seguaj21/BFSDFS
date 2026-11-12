"""Run with: python test_graphs.py. Do not change expected outputs."""
from main import make_graph_1, make_graph_2, make_graph_3


def check(label, actual, expected):
    assert actual == expected, f'{label}: expected {expected}, got {actual}'
    print('PASS:', label)


g = make_graph_1()
check('Graph 1 DFS', g.dfs('A'), ['A', 'B', 'D', 'E', 'F', 'C'])
check('Graph 1 BFS', g.bfs('A'), ['A', 'B', 'C', 'D', 'E', 'F'])
check('Graph 1 neighbors A', g.adj['A'], ['B', 'C'])
check('Graph 1 neighbors E', g.adj['E'], ['B', 'F'])

g = make_graph_2()
check('Graph 2 DFS', g.dfs(0), [0, 1, 3, 2])
check('Graph 2 BFS', g.bfs(0), [0, 1, 2, 3])

g = make_graph_3()
check('Graph 3 DFS from A', g.dfs('A'), ['A', 'B', 'C'])
check('Graph 3 BFS from A', g.bfs('A'), ['A', 'B', 'C'])
check('Graph 3 isolated DFS', g.dfs('Z'), ['Z'])
check('Graph 3 isolated BFS', g.bfs('Z'), ['Z'])

g.add_edge('A', 'B')
check('No duplicate edge', g.adj['A'], ['B'])
print('\nAll tests passed!')
