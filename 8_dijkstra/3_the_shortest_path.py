"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e9)


def dijkstra(source, graph, dest):
    distance = [INF for _ in range(len(graph))]
    min_heap = []
    distance[source] = 0
    heapq.heappush(min_heap, (0, source))
    while min_heap:
        cur_dist, u = heapq.heappop(min_heap)
        if cur_dist != distance[u]:
            continue
        for v, w in graph[u]:
            if cur_dist + w < distance[v]:
                distance[v] = cur_dist + w
                heapq.heappush(min_heap, (distance[v], v))
    return distance[dest]


if __name__ == '__main__':
    num_testcase = int(input())
    for _ in range(num_testcase):
        name_id_map = {}
        city = int(input())
        graph = [[] for k in range(city)]
        for i in range(city):
            city_name = input()
            name_id_map[city_name] = i
            adjacency_city = int(input())
            for k in range(adjacency_city):
                v, w = map(int, input().split())
                graph[i].append((v - 1, w))
        query_num = int(input())
        for index in range(query_num):
            name1, name2 = input().split()
            u = name_id_map[name1]
            v = name_id_map[name2]
            print(dijkstra(u, graph, v))

        if _ != num_testcase - 1:
            input()
