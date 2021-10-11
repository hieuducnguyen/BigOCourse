"""
Link:
Time complexity: O(V^2)
Space complexity: O(n)
"""

import heapq

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def dfs(graph, i, j, visited, n, m):
    stack = []
    visited[i][j] = True
    stack.append((i, j))
    size = 1
    is_out = False
    while len(stack) != 0:
        source = stack.pop()
        if source[1] == 0 or source[1] == m - 1 or source[0] == 0 or source[0] == n - 1:
            is_out = True
        for direct in range(4):
            new_i = source[0] + dr[direct]
            new_j = source[1] + dc[direct]
            if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j] and graph[new_i][new_j] == '.':
                size += 1
                visited[new_i][new_j] = True
                stack.append((new_i, new_j))
    return 0 if is_out else size


def dfs_remove_lake(graph, i, j, n, m):
    visited = [[False for i in range(m)] for j in range(n)]
    stack = []
    visited[i][j] = True
    stack.append((i, j))
    graph[i][j] = "*"
    num_replace = 1
    while len(stack) != 0:
        source = stack.pop()
        for direct in range(4):
            new_i = source[0] + dr[direct]
            new_j = source[1] + dc[direct]
            if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j] and graph[new_i][new_j] == '.':
                visited[new_i][new_j] = True
                stack.append((new_i, new_j))
                graph[new_i][new_j] = "*"
                num_replace += 1
    return num_replace


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(input()))
    visited = [[False for i in range(m)] for j in range(n)]
    total_lake = 0
    lake_list = []
    heap = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == '.':
                size = dfs(graph, i, j, visited, n, m)
                if size > 0:
                    total_lake += 1
                    lake_list.append((size, i, j))
                    heapq.heappush(heap, (size, i, j))
    need_remove = total_lake - k
    num_replace = 0
    for _ in range(need_remove):
        remove_lake = heapq.heappop(heap)
        num_replace += dfs_remove_lake(graph, remove_lake[1], remove_lake[2], n, m)

    print(num_replace)
    for i in range(len(graph)):
        print("".join(graph[i]))
