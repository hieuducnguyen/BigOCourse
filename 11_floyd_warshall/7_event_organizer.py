"""
Link: https://www.codechef.com/problems/MAXCOMP
Time complexity: O(T * V^3)
Space complexity: O(T * V^3)
Author: Nguyen Duc Hieu
"""

NEG_INF = -int(1e10)


def floyd_warshall(graph):
    V = len(graph)
    for k in range(V):
        for i in range(V):
            if graph[i][k] == NEG_INF: continue
            for j in range(V):
                if graph[k][j] != NEG_INF and graph[i][j] < graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N = int(input())
        graph = [[0 if i >= j else NEG_INF for i in range(49)] for j in range(49)]
        for i in range(N):
            S, E, C = map(int, input().split())
            if graph[S][E] < C:
                graph[S][E] = C
        floyd_warshall(graph)
        print(graph[0][48])
