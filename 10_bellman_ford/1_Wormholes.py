"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=499
Time complexity: O(T * N * M)
Space complexity: O(T * (N + M))
Author: Nguyen Duc Hieu
"""

INF = int(1e10)

if __name__ == '__main__':
    test_cast = int(input())
    for i in range(test_cast):
        N, M = map(int, input().split())
        edge_list = []
        for i in range(M):
            u, v, w = map(int, input().split())
            edge_list.append((u, v, w))
        dist = [INF] * N
        dist[0] = 0
        change = False
        for v in range(N):
            change = False
            for u, v, w in edge_list:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    change = True
        print("possible" if change else "not possible")
