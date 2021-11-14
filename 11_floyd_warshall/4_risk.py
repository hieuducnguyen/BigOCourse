"""
Link:
Time complexity: O(T * V^3)
Space complexity: O(T * V^3)
Author: Nguyen Duc Hieu
"""
INF = int(1e10)


def floy_warshall(graph):
    num_vertex = len(graph)
    for k in range(num_vertex):
        for i in range(num_vertex):
            if graph[i][k] == INF:
                continue
            for j in range(num_vertex):
                if graph[k][j] != INF and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


if __name__ == '__main__':
    test_case = 0
    while True:
        try:
            test_case += 1
            graph = [[INF for i in range(21)] for j in range(21)]
            for i in range(21):
                graph[i][i] = 0
            for i in range(1, 20):
                input_data = list(map(int, input().split()))
                for k in range(1, len(input_data)):
                    graph[i][input_data[k]] = 1
                    graph[input_data[k]][i] = 1
            dist = floy_warshall(graph)
            Q = int(input())
            print("Test Set #%s" % test_case)
            for i in range(Q):
                source, dest = map(int, input().split())
                print("{:2} to {:2}: {}".format(source, dest, dist[source][dest]))
            print()
        except EOFError as e:
            break
