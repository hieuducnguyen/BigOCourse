"""
Link: https://vjudge.net/problem/UVA-10171
Time complexity: O(T * (E * log(V))
Space complexity: O(T * (E + V))
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def dijkstra(graph, start, places):
    dist = dict()
    for vertex in places:
        dist[vertex] = INF
    dist[start] = 0
    min_heap = [(0, start)]
    while min_heap:
        cur_dist, source = heapq.heappop(min_heap)
        if cur_dist > dist[source]: continue
        for adjacency, distance in graph[source]:
            if dist[source] + distance < dist[adjacency]:
                dist[adjacency] = dist[source] + distance
                heapq.heappush(min_heap, (dist[adjacency], adjacency))
    return dist


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        edge_list_map = {'Y': [], 'M': []}
        places = set()
        for n in range(N):
            young, direct, X, Y, C = input().split()
            edge_list = edge_list_map.get(young)
            edge_list.append((X, Y, int(C)))
            places.update([X, Y])
            if direct == "B":
                edge_list.append((Y, X, int(C)))
        my_place, his_place = input().split()
        places.update([my_place, his_place])
        young_graph = dict()
        old_graph = dict()
        for place in places:
            young_graph[place] = []
            old_graph[place] = []
        for X, Y, C in edge_list_map.get("Y"):
            young_graph[X].append((Y, C))
        for X, Y, C in edge_list_map.get("M"):
            old_graph[X].append((Y, C))

        young_dist = dijkstra(young_graph, my_place, places)
        old_dist = dijkstra(old_graph, his_place, places)
        min_dist = INF
        list_place = []
        for place in places:
            if young_dist.get(place, INF) != INF and old_dist.get(place, INF) != INF:
                if young_dist.get(place) + old_dist.get(place) < min_dist:
                    min_dist = young_dist.get(place) + old_dist.get(place)
                    list_place = [place]
                elif young_dist.get(place) + old_dist.get(place) == min_dist:
                    list_place.append(place)
        if min_dist == INF:
            print("You will never meet.")
        else:
            list_place.sort()
            print(min_dist, end=" ")
            print(*list_place, sep=" ")
