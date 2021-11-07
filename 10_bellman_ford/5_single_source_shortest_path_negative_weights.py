"""
Link: https://open.kattis.com/problems/shortestpath1
Time complexity: O(T * N * M)
Space complexity: O(T * (N + M))
Author: Nguyen Duc Hieu
"""
INF = int(1e10)


def bellman_ford(source, edge_list, N):
    dist = [INF] * N
    dist[source] = 0
    for i in range(N - 1):
        change = False
        for u, v, w in edge_list:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                change = True
        if not change:
            break
    for i in range(N):
        change = False
        for u, v, w in edge_list:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                change = True
        if not change:
            break
    return dist


if __name__ == '__main__':
    while True:
        n, m, q, s = map(int, input().split())
        if n == m == q == s == 0:
            break
        edge_list = []
        for i in range(m):
            u, v, w = map(int, input().split())
            edge_list.append((u, v, w))
        dist = bellman_ford(s, edge_list, n)
        for i in range(q):
            query = int(input())
            if dist[query] == -INF:
                print("-Infinity")
            elif dist[query] == INF:
                print("Impossible")
            else:
                print(dist[query])
        print()
