"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e9)


def dijkstra(S, T, graph):
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


if __name__ == '__main__':
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
        distance = dijkstra(S - 1, T - 1, graph)
        if distance == INF:
            print(-1)
        else:
            print(distance)
