"""
Link: https://www.spoj.com/problems/UCV2013B/
Time complexity: O(T * N * (M * V + Q)) M is num edge
Space complexity: O(T * (E + V))
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
    test_case = 0
    while True:
        N = int(input())
        if N == 0:
            break
        name_list = []
        edge_list = []
        for i in range(N):
            distance = input().split()
            name = distance.pop(0)
            name_list.append(name)
            distance_list = list(map(int, distance))
            for j in range(len(distance_list)):
                if distance_list[j] != 0:
                    edge_list.append((i, j, distance_list[j]))
        Q = int(input())
        query_list = []
        source_set = set()
        for i in range(Q):
            u, v = map(int, input().split())
            query_list.append((u, v))
            source_set.add(u)
        distance_query = [[] for k in range(N)]
        for source in source_set:
            distance_query[source] = bellman_ford(source, edge_list, N)
        test_case += 1
        print("Case #{}:".format(test_case))
        for query in query_list:
            source = query[0]
            dest = query[1]
            if distance_query[source][dest] == INF:
                print("{}-{} {}".format(name_list[source], name_list[dest], "NOT REACHABLE"))
            elif distance_query[source][dest] == -INF:
                print("NEGATIVE CYCLE")
            else:
                print("{}-{} {}".format(name_list[source], name_list[dest], distance_query[source][dest]))
