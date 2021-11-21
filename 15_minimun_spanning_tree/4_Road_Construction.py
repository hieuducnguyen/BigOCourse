"""
Link: https://lightoj.com/problem/road-construction
Time complexity: O(M * Log(N)) N: num city
Space complexity: O(M + N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def prim(graph, name_set):
    visited = dict()
    dist = dict()
    first_city = ""
    for name in name_set:
        visited[name] = False
        dist[name] = INF
        first_city = name
    min_heap = [(0, first_city)]
    dist[first_city] = 0
    while min_heap:
        weight_source, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                heapq.heappush(min_heap, (weight, adjacency))
    return dist


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        input()
        M = int(input())
        graph = dict()
        name_set = set()
        for m in range(M):
            city_1, city_2, cost = input().split()
            graph[city_1] = graph.get(city_1, [])
            graph[city_2] = graph.get(city_2, [])
            graph[city_1].append((city_2, int(cost)))
            graph[city_2].append((city_1, int(cost)))
            name_set.add(city_1)
            name_set.add(city_2)
        dist = prim(graph, name_set)
        total_cost = 0
        for name in name_set:
            if dist[name] == INF:
                print("Case {}: {}".format(tc + 1, "Impossible"))
                break
            total_cost += dist[name]
        else:
            print("Case {}: {}".format(tc + 1, total_cost))
