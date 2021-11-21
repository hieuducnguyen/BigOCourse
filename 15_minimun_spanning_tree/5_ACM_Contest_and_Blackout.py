"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1541
Time complexity: O(T * N * M * Log(N))
Space complexity: O(T *(M + N))
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def prim(graph, N):
    dist = [INF] * N
    visited = [False] * N
    dist[0] = 0
    min_heap = [(0, 0)]
    path = [(-1, 0)] * N
    while min_heap:
        weight_source, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for i in range(len(graph[source])):
            adjacency, weight = graph[source][i][0], graph[source][i][1]
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                heapq.heappush(min_heap, (weight, adjacency))
                path[adjacency] = (source, i)
    return dist, path


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N, M = map(int, input().split())
        graph = [[] for _ in range(N)]
        for m in range(M):
            A, B, C = map(int, input().split())
            graph[A - 1].append((B - 1, C))
            graph[B - 1].append((A - 1, C))
        MST_dist, MST_path = prim(graph, N)
        MST_distance = sum(MST_dist)
        second_MST_distance = INF
        for i in range(1, len(MST_path)):
            source, dest, index = MST_path[i][0], i, MST_path[i][1]
            temp = graph[source][index]
            graph[source][index] = (temp[0], INF)
            temp_dist, temp_path = prim(graph, N)
            second_MST_distance = min(sum(temp_dist), second_MST_distance)
            graph[source][index] = temp
        print(MST_distance, second_MST_distance)
