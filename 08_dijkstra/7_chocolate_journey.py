"""
Link: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/successful-marathon-0691ec04/
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def dijkstra(source, graph):
    distance = [INF for _ in range(len(graph))]
    min_heap = []
    heapq.heappush(min_heap, (0, source))
    distance[source] = 0
    while min_heap:
        cur_dist, u = heapq.heappop(min_heap)
        if cur_dist != distance[u]:
            continue
        for v, w in graph[u]:
            if cur_dist + w < distance[v]:
                distance[v] = cur_dist + w
                heapq.heappush(min_heap, (distance[v], v))
    return distance


if __name__ == '__main__':
    N, M, k, x = map(int, input().split())
    socola_vertex = [int(value) - 1 for value in input().split()]
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, d = map(int, input().split())
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))
    A, B = map(int, input().split())
    distance_from_A = dijkstra(A - 1, graph)
    distance_from_B = dijkstra(B - 1, graph)
    min_time = INF
    for i in socola_vertex:
        if distance_from_A[i] != INF and distance_from_B[i] != INF and distance_from_B[i] <= x:
            min_time = min(min_time, distance_from_A[i] + distance_from_B[i])
    if min_time == INF:
        print(-1)
    else:
        print(min_time)
