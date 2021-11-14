"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def prim(graph, V, city_names):
    dist = dict()
    visited = dict()
    source = ""
    for name in city_names:
        dist[name] = INF
        visited[name] = False
        source = name
    min_heap = [(0, source)]
    dist[source] = 0
    while min_heap:
        distance, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                heapq.heappush(min_heap, (dist[adjacency], adjacency))
    return dist


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        input()
        M = int(input())
        name_city = set()
        edge_list = []
        for m in range(M):
            city_1, city_2, cost = input().split()
            name_city.add(city_1)
            name_city.add(city_2)
            edge_list.append((city_1, city_2, int(cost)))
        V = len(name_city)
        graph = dict()
        for city_1, city_2, cost in edge_list:
            if city_1 not in graph:
                graph[city_1] = []
            if city_2 not in graph:
                graph[city_2] = []
            graph.get(city_1).append((city_2, cost))
            graph.get(city_2).append((city_1, cost))
        cost_map = prim(graph, V, name_city)
        total_cost = 0
        for name in name_city:
            if cost_map[name] == INF:
                print("Case {}: Impossible".format(t + 1))
                break
            total_cost += cost_map[name]
        else:
            print("Case {}: {}".format(t + 1, total_cost))
