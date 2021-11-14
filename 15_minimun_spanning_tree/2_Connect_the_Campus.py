"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

import math

INF = int(1e10)


def prim(graph, N):
    dist = [INF] * N
    min_heap = [(0, 0)]
    dist[0] = 0
    visited = [False] * N
    while min_heap:
        weight, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                heapq.heappush(min_heap, (weight, adjacency))
    return dist


if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            list_building = []
            for i in range(N):
                x, y = map(int, input().split())
                list_building.append((x, y))
            available = []
            M = int(input())
            graph = [[] for _ in range(N)]
            for i in range(M):
                building_1, building_2 = map(int, input().split())
                # print(building_1, building_2)
                available.append((building_1 - 1, building_2 - 1))
                available.append((building_2 - 1, building_1 - 1))
                graph[building_1 - 1].append((building_2 - 1, 0))
                graph[building_2 - 1].append((building_1 - 1, 0))
                # print(available)
                # print(i)
            for i in range(N):
                for j in range(i + 1, N):
                    distance = math.sqrt(
                        (list_building[i][0] - list_building[j][0]) ** 2 + (
                                list_building[i][1] - list_building[j][1]) ** 2)
                    graph[i].append((j, distance))
                    graph[j].append((i, distance))
            dist = prim(graph, N)
            print("{:.2f}".format(sum(dist)))
        except EOFError:
            break
