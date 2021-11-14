"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def prim(graph):
    dist = [INF] * N
    visited = [False] * N
    min_heap = [(0, 0)]
    dist[0] = 0
    while min_heap:
        distance, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        for adjacency, w in graph[node]:
            if not visited[adjacency] and dist[adjacency] > w:
                dist[adjacency] = w
                heapq.heappush(min_heap, (dist[adjacency], adjacency))

    return dist


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for u in range(M):
        i, j, k = map(int, input().split())
        graph[i - 1].append((j - 1, k))
        graph[j - 1].append((i - 1, k))
    dist = prim(graph)
    print(sum(dist))
