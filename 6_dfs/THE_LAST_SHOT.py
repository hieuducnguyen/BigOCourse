"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def dfs(graph, boom):
    stack = []
    visited = [False for _ in range(N)]
    visited[boom] = True
    stack.append(boom)
    size = 1
    while len(stack) != 0:
        source = stack.pop()
        for adjacency in graph[source]:
            if not visited[adjacency]:
                visited[adjacency] = True
                stack.append(adjacency)
                size += 1
    return size


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    list_boom = []
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        list_boom.append(u - 1)
    max_size = -1
    for boom in list_boom:
        max_size = max(max_size, dfs(graph, boom))
    print(max_size)
