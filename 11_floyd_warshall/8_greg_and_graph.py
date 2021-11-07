"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

INF = int(1e10)


def floyd_warshall(graph, N):
    dist = [[INF for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = graph[i][j]
    for k in range(N):
        for i in range(N):
            if dist[i][k] == INF:
                continue
            for j in range(N):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    total_dist_edge = 0
    for i in range(N):
        for j in range(N):
            if dist[i][j] != INF:
                total_dist_edge += dist[i][j]
    return total_dist_edge


def remove_vertex(graph, removing_vertex):
    for i in range(N):
        graph[removing_vertex][i] = INF
        graph[i][removing_vertex] = INF


if __name__ == '__main__':
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    remove_vertex_list = list(map(int, input().split()))
    result = []
    for removing_vertex in remove_vertex_list:
        total_dist = floyd_warshall(graph, N)
        result.append(total_dist)
        remove_vertex(graph, removing_vertex - 1)
    print(*result, sep=" ")
