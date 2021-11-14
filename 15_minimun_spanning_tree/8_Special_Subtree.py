"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def prim(graph, source, N):
    dist = [INF] * N
    visited = [False] * N
    min_heap = [(0, source)]
    dist[source] = 0
    while min_heap:
        distance, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                heapq.heappush(min_heap, (weight, adjacency))
    return dist


if __name__ == '__main__':
    N, M = map(int, input().split())
    dist = [[INF] * N for _ in range(N)]
    for m in range(M):
        x, y, cost = map(int, input().split())
        if dist[x - 1][y - 1] > cost:
            dist[x - 1][y - 1] = cost
            dist[y - 1][x - 1] = cost
    source = int(input()) - 1
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if dist[i][j] == INF: continue
            graph[i].append((j, dist[i][j]))
            graph[j].append((i, dist[i][j]))
    dist = prim(graph, source, N)
    total = 0
    for sub_dist in dist:
        if sub_dist != INF:
            total += sub_dist
    print(total)
