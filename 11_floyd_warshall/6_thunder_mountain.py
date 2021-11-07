"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

import math

INF = int(1e10)


def distance(u, v, vertex_list):
    return math.sqrt((vertex_list[u][0] - vertex_list[v][0]) ** 2 + (vertex_list[u][1] - vertex_list[v][1]) ** 2)


def floyd_warshall(vertex_list, N):
    dist = [[INF for u in range(N)] for v in range(N)]
    for u in range(N):
        for v in range(N):
            if u == v:
                dist[u][v] = 0
            else:
                distance_u_v = distance(u, v, vertex_list)
                if distance_u_v <= 10:
                    dist[u][v] = distance_u_v
                    dist[v][u] = distance_u_v
    for k in range(N):
        for i in range(N):
            if dist[i][k] == INF:
                continue
            for j in range(N):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == '__main__':
    num_testcase = int(input())
    for i in range(num_testcase):
        print("Case #{}:".format(i + 1))
        N = int(input())
        vertex_list = []
        for k in range(N):
            x, y = map(int, input().split())
            vertex_list.append((x, y))
        dist = floyd_warshall(vertex_list, N)
        max_distance = 0
        for u in range(N):
            max_distance = max(max_distance, max(dist[u]))
            if max_distance == INF:
                print("Send Kurdy")
                print()
                break
        if max_distance == INF:
            continue
        else:
            print("{:.4f}".format(max_distance, 4))
            print()
