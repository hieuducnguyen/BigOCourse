"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1187
Time complexity: O(T * C^3)
Space complexity: O(T * C^2)
Author: Nguyen Duc Hieu
"""

INF = int(1e10)


def floyd_warshall(graph, num_vertex, cost_party):
    dist = [[(INF, 0) for i in range(num_vertex)] for j in range(num_vertex)]
    for i in range(num_vertex):
        for j in range(num_vertex):
            if graph[i][j] != INF:
                dist[i][j] = (graph[i][j], max(cost_party[i], cost_party[j]))
        for e in range(2):
            for k in range(num_vertex):
                for i in range(num_vertex):
                    if dist[i][k][0] == INF:
                        continue
                    for j in range(num_vertex):
                        cost_party_in_place = max(dist[i][k][1], dist[k][j][1])
                        if dist[k][j][0] != INF and dist[i][j][0] + dist[i][j][1] > dist[i][k][0] + dist[k][j][
                            0] + cost_party_in_place:
                            dist[i][j] = (dist[i][k][0] + dist[k][j][0], cost_party_in_place)
    return dist


if __name__ == '__main__':
    num_testcase = 0
    first = True
    while True:
        C, R, Q = map(int, input().split())
        if C == 0 and R == 0 and Q == 0:
            break
        if not first:
            print()
        first = False
        num_testcase += 1
        print("Case #%s" % num_testcase)
        graph = [[INF for i in range(C)] for j in range(C)]
        cost_party = list(map(int, input().split()))
        for i in range(C):
            graph[i][i] = 0
        for i in range(R):
            u, v, w = map(int, input().split())
            if graph[u - 1][v - 1] < w:
                continue
            graph[u - 1][v - 1] = w
            graph[v - 1][u - 1] = w
        dist = floyd_warshall(graph, C, cost_party)
        for i in range(Q):
            u, v = map(int, input().split())
            print(dist[u - 1][v - 1][0] + dist[u - 1][v - 1][1] if dist[u - 1][v - 1][0] != INF else -1)
