"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3296
Time complexity: O(T * E * log(V))
Space complexity: O(T * (E + V))
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def dijkstra(S, D, graph):
    N = len(graph)
    dist = [INF for _ in range(N)]
    min_heap = []
    heapq.heappush(min_heap, (0, S))
    dist[S] = 0
    while min_heap:
        cur_dist, u = heapq.heappop(min_heap)
        if dist[u] != cur_dist:
            continue
        if u == D:
            break
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(min_heap, (dist[v], v))
    return dist


if __name__ == '__main__':
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        S, D = map(int, input().split())
        graph_S = [[] for _ in range(N)]
        graph_D = [[] for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, input().split())
            graph_S[U].append((V, P))
            graph_D[V].append((U, P))
        dist_S = dijkstra(S, D, graph_S)
        dist_D = dijkstra(D, S, graph_D)
        shortest_path = dist_S[D]
        if shortest_path == INF:
            print(-1)
            continue
        new_graph = [[] for _ in range(N)]
        for u in range(len(graph_S)):
            for v, w in graph_S[u]:
                if dist_S[u] + w + dist_D[v] != shortest_path:
                    new_graph[u].append((v, w))
        dist = dijkstra(S, D, new_graph)
        if dist[D] == INF:
            print(-1)
        else:
            print(dist[D])
