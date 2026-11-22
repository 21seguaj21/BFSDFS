"""CSC 225 - Graph search starter code. Finish the TODO sections."""
from collections import deque


class Graph:
    def __init__(self):
        # A dictionary: vertex -> list of neighbors
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def dfs(self, start):
        """Return a DFS visitation list starting at start."""
        visited = set()
        order = []

        def helper(u):
            visited.add(u)
            order.append(u)
            for neighbor in self.adj[u]:
                if neighbor not in visited:
                    helper(neighbor)

        helper(start)
        return order

    def bfs(self, start):
        """Return a BFS visitation list starting at start."""
        visited = {start}
        order = []
        queue = deque([start])

        while queue:
            u = queue.popleft()
            order.append(u)
            for neighbor in self.adj[u]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order