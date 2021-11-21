"""
Link: https://www.hackerrank.com/challenges/bfsshortreach/problem
Time complexity: O(Q * (N + M))
Space complexity: O(Q * (N + M))
Q: num test case
N: vertex
M: edge
"""

from collections import deque


class Graph:
    def __init__(self, V, E=0):
        self.V = V
        if E > 0:
            self.alist = {key: list() for key in range(1, V + 1)}

    def add_edge(self, source, dest):
        self.alist.get(source).append(dest)
        self.alist.get(dest).append(source)

    def bfs(self, source):
        queue = deque()
        visited = [-1] * (self.V + 1)
        visited[source] = 0
        queue.append(source)
        while queue:
            source = queue.popleft()
            for adjacency in self.alist[source]:
                if visited[adjacency] < 0:
                    visited[adjacency] = visited[source] + 6
                    queue.append(adjacency)

        self.distance = visited

    def answer(self, source):
        self.bfs(source)
        result = " ".join(str(self.distance[x]) for x in range(1, len(self.distance)) if x != source)
        return result


if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        N, M = map(int, input().split())
        my_graph = Graph(N, M)
        for i in range(M):
            u, v = map(int, input().split())
            my_graph.add_edge(u, v)
            my_graph.add_edge(v, u)
        S = int(input())
        print(my_graph.answer(S))
