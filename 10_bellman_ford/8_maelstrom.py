"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=364
Time complexity: O(E * log(V))
Space complexity: O(E + V)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def dijkstra(source, graph):
    V = len(graph)
    dist = [INF] * V
    dist[source] = 0
    min_heap = [(0, source)]
    while min_heap:
        cur_dist, source = heapq.heappop(min_heap)
        if dist[source] != cur_dist:
            continue
        for adjacency, distance in graph[source]:
            if dist[source] + distance < dist[adjacency]:
                dist[adjacency] = dist[source] + distance
                heapq.heappush(min_heap, (dist[adjacency], adjacency))
    return dist


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(N)]
    for i in range(1, N):
        distance_list = input().split()
        for j in range(i):
            if distance_list[j] != "x":
                distance = int(distance_list[j])
                graph[i].append((j, distance))
                graph[j].append((i, distance))
    dist = dijkstra(0, graph)
    print(max(dist))
