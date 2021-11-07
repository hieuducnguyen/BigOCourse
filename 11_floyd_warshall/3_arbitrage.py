"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

NEG_INF = -int(1e10)


def floyd_warshall(graph, N):
    for k in range(N):
        for i in range(N):
            if graph[i][k] == NEG_INF:
                continue
            for j in range(N):
                if graph[k][j] != NEG_INF and graph[i][j] < graph[i][k] * graph[k][j]:
                    graph[i][j] = graph[i][k] * graph[k][j]
    # print(graph)
    for i in range(N):
        if graph[i][i] > 1:
            return True
    return False


if __name__ == '__main__':
    case = 0
    while True:
        N = int(input())
        if N == 0:
            break
        case += 1
        name_currency_id_map = {}
        id_name_currency_map = {}
        id_currency = -1
        for _ in range(N):
            name_currency = input()
            id_currency += 1
            name_currency_id_map[name_currency] = id_currency
            id_name_currency_map[id_currency] = name_currency
        graph = [[NEG_INF for _ in range(N)] for _ in range(N)]
        for i in range(N):
            graph[i][i] = 0
        M = int(input())
        for i in range(M):
            name_source, val, name_dist = input().split()
            graph[name_currency_id_map[name_source]][name_currency_id_map[name_dist]] = float(val)
        cycle = floyd_warshall(graph, N)
        print("Case {}: {}".format(case, "Yes" if cycle else "No"))
        input()
