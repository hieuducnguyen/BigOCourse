"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=40
Time complexity: O(T * V ^ 3) V: num currency money
Space complexity: O(T * V ^ 3)
Author: Nguyen Duc Hieu
"""
NEG_INF = -int(1e10)


def floyd_warshall(graph):
    V = len(graph)
    for k in range(V):
        for i in range(V):
            if graph[i][k] == NEG_INF: continue
            for j in range(V):
                if graph[k][j] != NEG_INF and graph[i][j] < graph[i][k] * graph[k][j]:
                    graph[i][j] = graph[i][k] * graph[k][j]


if __name__ == '__main__':
    tc = 0
    while True:
        N = int(input())
        if N == 0:
            break
        tc += 1
        list_currency = []
        for i in range(N):
            list_currency.append(input())
        graph = [[1 if i == j else NEG_INF for i in range(N)] for j in range(N)]
        M = int(input())
        for m in range(M):
            currency_1, trade, currency_2 = input().split()
            graph[list_currency.index(currency_1)][list_currency.index(currency_2)] = float(trade)
        floyd_warshall(graph)
        input()
        for i in range(N):
            if graph[i][i] > 1:
                print("Case {}: {}".format(tc, "Yes"))
                break
        else:
            print("Case {}: {}".format(tc, "No"))
