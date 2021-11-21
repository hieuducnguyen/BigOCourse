"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1927
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def dijkstra(S, T, graph):
    dist = [INF for _ in range(len(graph))]
    dist[S] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, S))
    while min_heap:
        cur_dist, u = heapq.heappop(min_heap)
        if cur_dist != dist[u]:
            continue
        if u == T:
            break
        for v, w in graph[u]:
            if cur_dist + w < dist[v]:
                dist[v] = cur_dist + w
                heapq.heappush(min_heap, (dist[v], v))
    return dist[T]


if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        N, M, S, T = map(int, input().split())
        graph = [[] for _ in range(N)]
        for i in range(M):
            a, b, w = map(int, input().split())
            graph[a].append((b, w))
            graph[b].append((a, w))
        distace = dijkstra(S, T, graph)
        if distace == INF:
            print("Case #%s: %s" % (_ + 1, "unreachable"))
        else:
            print("Case #%s: %s" % (_ + 1, distace))
