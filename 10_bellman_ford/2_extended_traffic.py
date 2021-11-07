"""
Link: https://lightoj.com/problem/extended-traffic
Time complexity: O(T * N * M)
Space complexity: O(T * (N + M))
Author: Nguyen Duc Hieu
"""

INF = int(1e10)


def bellman_ford(source, N, edge_list):
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
    T = int(input())
    for t in range(T):
        input()
        print("Case {}:".format(t + 1))
        N = int(input())
        traffic_jam = list(map(int, input().split()))
        M = int(input())
        edge_list = []
        for i in range(M):
            u, v = map(int, input().split())
            edge_list.append((u - 1, v - 1, (traffic_jam[v - 1] - traffic_jam[u - 1]) ** 3))
        dist = bellman_ford(0, N, edge_list)
        Q = int(input())
        for q in range(Q):
            dest = int(input())
            print(dist[dest - 1] if dist[dest - 1] >= 3 and dist[dest - 1] != INF else "?")
