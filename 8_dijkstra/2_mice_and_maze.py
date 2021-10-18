"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e9)


def dijkstra(E, graph, dist, T):
    min_heap = []
    dist[E] = 0
    heapq.heappush(min_heap, (dist[E], E))
    while min_heap:
        cur_distance, u = heapq.heappop(min_heap)
        if dist[u] != cur_distance:
            continue
        for v, w in graph[u]:
            if cur_distance + w < dist[v] and cur_distance + w <= T:
                dist[v] = cur_distance + w
                heapq.heappush(min_heap, (dist[v], v))


if __name__ == '__main__':
    N = int(input())
    E = int(input())
    T = int(input())
    M = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[b - 1].append((a - 1, w))
    dist = [INF for _ in range(N)]
    dijkstra(E - 1, graph, dist, T)
    print(N - dist.count(INF))
