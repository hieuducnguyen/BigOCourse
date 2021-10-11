"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""
import sys

sys.setrecursionlimit(10 ** 4 + 5)


def dfs_check_cycle(graph, i, N, path_visited, visited):
    path_visited[i] = True
    visited[i] = True
    for edge in graph[i]:
        if not path_visited[edge]:
            if dfs_check_cycle(graph, edge, N, path_visited, visited):
                return True
        else:
            return True
    path_visited[i] = False
    return False


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        graph = [[] for i in range(N)]
        for i in range(M):
            u, v = map(int, input().split())
            graph[u - 1].append(v - 1)
        visited = [False for i in range(N)]
        is_cycle = True
        for i in range(N):
            if not visited[i]:
                inner_visited = [False for i in range(N)]
                is_cycle = dfs_check_cycle(graph, i, N, inner_visited, visited)
                for j in range(N):
                    if inner_visited[j]:
                        visited[j] = True
                if is_cycle:
                    break
        if is_cycle:
            print("YES")
        else:
            print("NO")
