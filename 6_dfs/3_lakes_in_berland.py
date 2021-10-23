"""
Link: https://codeforces.com/problemset/problem/723/D
Time complexity: O(V^2)
Space complexity: O(V^2)
"""

import heapq

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


class Lake:
    def __init__(self, size, cells):
        self.cells = cells
        self.size = size

    def __lt__(self, other):
        return self.size < other.size


def dfs(graph, i, j, visited, n, m):
    stack = []
    visited[i][j] = True
    stack.append((i, j))
    lake = [(i, j)]
    is_out = False
    while len(stack) != 0:
        source = stack.pop()
        if source[1] == 0 or source[1] == m - 1 or source[0] == 0 or source[0] == n - 1:
            is_out = True
        for direct in range(4):
            new_i = source[0] + dr[direct]
            new_j = source[1] + dc[direct]
            if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j] and graph[new_i][new_j] == '.':
                visited[new_i][new_j] = True
                stack.append((new_i, new_j))
                lake.append((new_i, new_j))
    return None if is_out else Lake(len(lake), lake)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(input()))
    visited = [[False for i in range(m)] for j in range(n)]
    total_lake = 0
    lake_list = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == '.':
                visited_lake = dfs(graph, i, j, visited, n, m)
                if visited_lake is not None:
                    total_lake += 1
                    lake_list.append(visited_lake)
    heapq.heapify(lake_list)
    need_remove = total_lake - k
    num_replace = 0
    for _ in range(need_remove):
        remove_lake = heapq.heappop(lake_list)
        for i, j in remove_lake.cells:
            graph[i][j] = "*"
            num_replace += 1

    print(num_replace)
    for i in range(len(graph)):
        print(*graph[i], sep="")
