"""
Link:
Time complexity: O(N + N -1 + Q)
Space complexity: O(N + N -1)
"""

INF = int(1e10)


def dfs(source, graph):
    distance = [INF for _ in range(len(graph))]
    stack = []
    distance[source] = 0
    stack.append(source)
    while stack:
        source = stack.pop()
        for adjacency in graph[source]:
            if distance[adjacency] == INF:
                distance[adjacency] = distance[source] + 1
                stack.append(adjacency)
    return distance


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    dist = dfs(0, graph)
    Q = int(input())
    min_distance = INF
    min_index = -1
    for i in range(Q):
        val = int(input())
        if dist[val - 1] < min_distance or dist[val - 1] == min_distance and min_index > val:
            min_distance = dist[val - 1]
            min_index = val
    print(min_index)
