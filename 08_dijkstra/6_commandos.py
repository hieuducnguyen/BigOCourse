"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1927
Time complexity: O(T * (E + V))
Space complexity: O(T * (E + V))
Author: Nguyen Duc Hieu
"""
from collections import deque


def bfs(s, graph):
    queue = deque()
    visited = [-1 for _ in range(len(graph))]
    queue.append(s)
    visited[s] = 0
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if visited[v] < 0:
                visited[v] = visited[u] + 1
                queue.append(v)
    return visited


if __name__ == '__main__':
    T = int(input())
    for _ in range(1, T + 1):
        N = int(input())
        R = int(input())
        graph = [[] for i in range(N)]
        for i in range(R):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        s, d = map(int, input().split())
        distance = bfs(s, graph)
        next_source_distance = bfs(d, graph)
        max_time = -1
        for k in range(N):
            if next_source_distance[k] != -1 and distance[k] != -1:
                max_time = max(max_time, next_source_distance[k] + distance[k])
        print("Case %s: %s" % (_, max_time))
