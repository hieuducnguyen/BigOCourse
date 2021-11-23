"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

import math

INF = int(1e10)


def distance(point_1, point_2):
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def prim(graph, N):
    visited = [False] * N
    dist = [INF] * N
    min_heap = [(0, 0)]
    dist[0] = 0
    while min_heap:
        weight_source, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                heapq.heappush(min_heap, (weight, adjacency))
    return sum(dist)


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        try:
            input()
            N = int(input())
            point_list = []
            for i in range(N):
                x, y = map(float, input().split())
                point_list.append((x, y))
            graph = [[] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    distance_two_point = distance(point_list[i], point_list[j])
                    graph[i].append((j, distance_two_point))
                    graph[j].append((i, distance_two_point))
            total_cost = prim(graph, N)
            print("{:.2f}".format(total_cost))
            print()
        except EOFError:
            break
