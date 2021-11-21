"""
Link: https://vn.spoj.com/problems/TRAFFICN/
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e9)


def dijkstra_1(S, T, graph):
    dist = [[INF for _ in range(len(graph))] for i in range(2)]
    dist[0][S] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, S, False))
    while min_heap:
        cur_dist, u, use_k = heapq.heappop(min_heap)
        if cur_dist > dist[use_k][u]:
            continue
        for v, w, flag in graph[u]:
            if not use_k or (use_k and not flag):
                if cur_dist + w < dist[use_k or flag][v]:
                    dist[use_k or flag][v] = cur_dist + w
                    heapq.heappush(min_heap, (dist[use_k or flag][v], v, use_k or flag))
    return min(dist[0][T], dist[1][T])


"""
Time complexity: O(E * Log V) ~~ (M + K) * log (2 * N)
Space complexity: O(E + V) ~~ O(M + K + N)
"""


def method_1():
    global d
    num_testcase = int(input())
    for _ in range(num_testcase):
        N, M, K, S, T = map(int, input().split())
        graph = [[] for i in range(N)]
        for i in range(M):
            d, c, l = map(int, input().split())
            graph[d - 1].append((c - 1, l, False))
        for i in range(K):
            u, v, q = map(int, input().split())
            graph[u - 1].append((v - 1, q, True))
            graph[v - 1].append((u - 1, q, True))
        distance = dijkstra_1(S - 1, T - 1, graph)
        if distance == INF:
            print(-1)
        else:
            print(distance)


def dijkstra_2(S, graph):
    min_heap = []
    distance = [INF for _ in range(len(graph))]
    heapq.heappush(min_heap, (0, S))
    distance[S] = 0
    while min_heap:
        cur_dist, source = heapq.heappop(min_heap)
        if distance[source] != cur_dist:
            continue
        for adjacency, weight in graph[source]:
            if distance[adjacency] > cur_dist + weight:
                distance[adjacency] = cur_dist + weight
                heapq.heappush(min_heap, (distance[adjacency], adjacency))
    return distance


"""
Time complexity: O(E * Log V + K) ~~ O(M * log (N) + K)
Space complexity: O(E + V) ~~ O(M + N)
"""


def method_2():
    num_testcase = int(input())
    for _ in range(num_testcase):
        N, M, K, S, T = map(int, input().split())
        graph_S = [[] for i in range(N)]
        graph_T = [[] for i in range(N)]
        for i in range(M):
            d, c, l = map(int, input().split())
            graph_S[d - 1].append((c - 1, l))
            graph_T[c - 1].append((d - 1, l))
        dist_S = dijkstra_2(S - 1, graph_S)
        dist_T = dijkstra_2(T - 1, graph_T)
        distance = dist_S[T - 1]
        for i in range(K):
            u, v, q = map(int, input().split())
            if dist_S[u - 1] != INF and dist_T[v - 1] != INF:
                distance = min(distance, dist_S[u - 1] + dist_T[v - 1] + q)
            if dist_S[v - 1] != INF and dist_T[u - 1] != INF:
                distance = min(distance, dist_S[v - 1] + dist_T[u - 1] + q)
        if distance == INF:
            print(-1)
        else:
            print(distance)


if __name__ == '__main__':
    method_2()
