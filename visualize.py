"""OPTIONAL: save an undirected graph as Graphviz DOT text.
No extra Python packages required. To render: dot -Tpng example_graph.dot -o example_graph.png
"""
from main import make_graph_1


def save_dot(g, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('graph G {\n')
        for vertex in g.adj:
            f.write(f'    "{vertex}";\n')
        seen = set()
        for vertex in g.adj:
            for neighbor in g.adj[vertex]:
                edge = frozenset([vertex, neighbor])
                if edge not in seen:
                    f.write(f'    "{vertex}" -- "{neighbor}";\n')
                    seen.add(edge)
        f.write('}\n')


if __name__ == '__main__':
    save_dot(make_graph_1(), 'example_graph.dot')
    print('Wrote example_graph.dot')
