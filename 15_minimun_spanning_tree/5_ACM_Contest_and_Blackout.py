"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def prim(graph, N):
    dist = [INF] * N
    visited = [False] * N
    path = [-1] * N
    dist[0] = 0
    min_heap = [(0, 0, 0)]
    while min_heap:
        cur_weight, source, source_of_source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                path[adjacency] = source
                heapq.heappush(min_heap, (weight, adjacency, source))
    return path, dist


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, M = map(int, input().split())
        graph = [[] for _ in range(N)]
        edge_list = []
        for m in range(M):
            A, B, C = map(int, input().split())
            graph[A - 1].append((B - 1, C))
            graph[B - 1].append((A - 1, C))
            edge_list.append((A - 1, B - 1, C))
            edge_list.append((B - 1, A - 1, C))
        path, dist = prim(graph, N)
        prim_graph = [[] for _ in range(N)]
        MST_edge_list = []
        for i in range(len(path)):
            if path[i] != -1:
                MST_edge_list.append((path[i], i))
                MST_edge_list.append((i, path[i]))
                prim_graph[i].append((path[i], dist[i]))
                prim_graph[path[i]].append((i, dist[i]))
        second_min_cost = INF
        for A, B, C in edge_list:
            if (A, B) in MST_edge_list or (B, A) in MST_edge_list:
                continue
            prim_graph[A].append((B, 0))
            prim_graph[B].append((A, 0))
            tmp_path, tmp_dist = prim(prim_graph, N)
            if second_min_cost > sum(tmp_dist) + C:
                second_min_cost = sum(tmp_dist) + C
            prim_graph[A].pop()
            prim_graph[B].pop()
        print("{} {}".format(sum(dist), second_min_cost))
