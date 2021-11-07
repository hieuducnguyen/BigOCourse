"""
Link: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/monks-business-day/
Time complexity: O(T * N * M)
Space complexity: O(T * (N + M))
Author: Nguyen Duc Hieu
"""
NEG_INF = -int(1e10)


def bellman_ford(source, edge_list, N):
    dist = [NEG_INF] * N
    dist[source] = 0
    change = False
    for i in range(N):
        change = False
        for u, v, w in edge_list:
            if dist[u] != NEG_INF and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                change = True
        if not change:
            break
    return change


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, M = map(int, input().split())
        edge_list = []
        for i in range(M):
            u, v, C = map(int, input().split())
            edge_list.append((u - 1, v - 1, C))
        print("Yes" if bellman_ford(0, edge_list, N) else "No")
