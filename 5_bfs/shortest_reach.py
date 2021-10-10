"""
Link:
Time complexity: O(N^2)
Space complexity: O(C * (N + M))
"""
from queue import Queue


def bfs(S, graph, N):
    visited = [False] * (N + 1)
    dist = [-1] * (N + 1)
    dist[S] = 0
    q = Queue()
    visited[S] = True
    q.put(S)
    while q.qsize() != 0:
        vertex = q.get()
        for adjacency in graph[vertex]:
            if not visited[adjacency]:
                dist[adjacency] = dist[vertex] + 1
                visited[adjacency] = True
                q.put(adjacency)
    for i in range(1, len(dist)):
        if i == S:
            continue
        if dist[i] == -1:
            print(-1, end="")
        else:
            print(dist[i] * 6, end="")
        if i != len(dist) - 1:
            print(" ", end="")


if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        N, M = map(int, input().split())
        graph = [[] for _ in range(N + 1)]
        for j in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        S = int(input())
        bfs(S, graph, N)
