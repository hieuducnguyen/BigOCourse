"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

NEG_INF = -int(1e10)


def floyd_warshall(graph):
    for k in range(49):
        for i in range(49):
            if graph[i][k] == NEG_INF:
                continue
            for j in range(49):
                if graph[k][j] != NEG_INF and graph[i][j] < graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = [[NEG_INF for i in range(49)] for k in range(49)]
        for i in range(49):
            for j in range(i, 49):
                graph[i][j] = 0
        for i in range(N):
            u, v, w = map(int, input().split())
            if graph[u][v] < w:
                graph[u][v] = w
        dist = floyd_warshall(graph)
        print(dist[0][48])
