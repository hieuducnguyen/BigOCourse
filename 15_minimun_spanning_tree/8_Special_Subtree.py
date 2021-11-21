"""
Link: https://www.hackerrank.com/challenges/primsmstsub/problem
Time complexity: O(M * Log(N))
Space complexity: O(M + N)
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
    graph = [[] for _ in range(N)]
    for m in range(M):
        x, y, cost = map(int, input().split())
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    source = int(input()) - 1
    dist = prim(graph, source, N)
    total = 0
    for sub_dist in dist:
        if sub_dist != INF:
            total += sub_dist
    print(total)
