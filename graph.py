"""CSC 225 - Graph search starter code. Finish the TODO sections."""
from collections import deque


class Graph:
    def __init__(self):
        # A dictionary: vertex -> list of neighbors
        self.adj = {}

    def add_vertex(self, v):
        # TODO: If v is not already in the dictionary, add v with an empty list.
        pass

    def add_edge(self, u, v):
        # TODO: Add both vertices (if necessary).
        # TODO: Add v to u's list, unless it is already there.
        # TODO: Add u to v's list, unless it is already there.
        # Assume u != v. The graph is undirected.
        pass

    def dfs(self, start):
        """Return a DFS visitation list starting at start."""
        # TODO: Make an empty visited set and an empty order list.
        # TODO: Define a recursive helper that visits a vertex and its
        #       unvisited neighbors in their stored order.
        # TODO: Start the helper at start and return order.
        # Assume start exists in self.adj.
        pass

    def bfs(self, start):
        """Return a BFS visitation list starting at start."""
        # TODO: Make an empty visited set, an empty order list, and a queue
        #       using deque imported from collections at the top of this file.
        # TODO: Add start to the queue and mark it visited immediately.
        # TODO: While the queue is not empty, remove the first vertex,
        #       append it to order, and enqueue any unvisited neighbors.
        #       Mark neighbors visited when they enter the queue.
        # TODO: Return order.
        # Assume start exists in self.adj.
        pass
