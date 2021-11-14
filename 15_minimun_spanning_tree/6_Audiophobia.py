"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

INF = int(1e10)


def floy_warshall(dist, V):
    for k in range(V):
        for i in range(V):
            if dist[i][k] == INF: continue
            for j in range(V):
                if dist[k][j] != INF and dist[i][j] > max(dist[i][k], dist[k][j]):
                    dist[i][j] = max(dist[i][k], dist[k][j])
    return dist


if __name__ == '__main__':
    test_case = 1
    while True:
        C, S, Q = map(int, input().split())
        if C == S == Q == 0:
            break
        dist = [[INF] * C for _ in range(C)]
        for i in range(C):
            dist[i][i] = 0
        for s in range(S):
            c1, c2, d = map(int, input().split())
            dist[c1 - 1][c2 - 1] = d
            dist[c2 - 1][c1 - 1] = d
        floy_warshall(dist, C)
        print("Case #{}".format(test_case))
        for q in range(Q):
            q1, q2 = map(int, input().split())
            if dist[q1 - 1][q2 - 1] != INF:
                print(dist[q1 - 1][q2 - 1])
            else:
                print("no path")
        print()
        test_case += 1
