"""
Link: https://www.beecrowd.com.br/judge/en/problems/view/1655
Time complexity: O(T * N * M)
Space complexity: O(T *(N + M))
Author: Nguyen Duc Hieu
"""


def count_percent(u, v, w, dist):
    return dist[u] * w


def bellman_ford(source, dest, edge_list, N):
    dist = [0 for _ in range(N)]
    dist[source] = 1
    for i in range(N - 1):
        for u, v, w in edge_list:
            val = count_percent(u, v, w, dist)
            if dist[u] != 0 and val > dist[v]:
                dist[v] = val
    return dist


if __name__ == '__main__':
    while True:
        input_line = input()
        if input_line == "0":
            break
        N, M = map(int, input_line.split())
        edge_list = []
        for i in range(M):
            a, b, p = map(int, input().split())
            edge_list.append((a - 1, b - 1, p / 100))
            edge_list.append((b - 1, a - 1, p / 100))
        dist = bellman_ford(0, N - 1, edge_list, N)
        print("%.6f percent" % (dist[N - 1] * 100))
