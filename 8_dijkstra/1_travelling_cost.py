"""
Link: https://www.spoj.com/problems/TRVCOST/
Time complexity: O(E * log(V)) = O (N * log(501))
Space complexity: O(E + V)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e9)
MAX = 501


def dijkstra(U, graph, dist):
    min_heap = []
    heapq.heappush(min_heap, (0, U))
    dist[U] = 0
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        if current_dist != dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(min_heap, (dist[v], v))


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(MAX)]
    for i in range(N):
        A, B, W = map(int, input().split())
        graph[A].append((B, W))
        graph[B].append((A, W))
    U = int(input())
    Q = int(input())
    dist = [INF for _ in range(MAX)]
    dijkstra(U, graph, dist)
    for i in range(Q):
        dest = int(input())
        if dist[dest] != INF:
            print(dist[dest])
        else:
            print("NO PATH")
