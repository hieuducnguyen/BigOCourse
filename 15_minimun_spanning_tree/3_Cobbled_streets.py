"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def prim(graph, N):
    dist = [INF] * N
    visited = [False] * N
    dist[0] = 0
    min_heap = [(0, 0)]
    while min_heap:
        weight, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                heapq.heappush(min_heap, (weight, adjacency))
    return dist


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        P = int(input())
        N = int(input())
        graph = [[] for _ in range(N)]
        M = int(input())
        for m in range(M):
            a, b, c = map(int, input().split())
            graph[a - 1].append((b - 1, c))
            graph[b - 1].append((a - 1, c))
        dist = prim(graph, N)
        print(sum(dist) * P)
