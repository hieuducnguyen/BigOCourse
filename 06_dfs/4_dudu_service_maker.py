"""
Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1610
Time complexity: O(T * (N + M))
Space complexity: O(T * (N + M))
"""
import sys

sys.setrecursionlimit(int(1e5))


def dfs(source, graph, visited):
    if visited[source] == 1:
        return True
    if visited[source] == 2:
        return False
    visited[source] = 1
    for adjacency in graph[source]:
        if dfs(adjacency, graph, visited):
            return True
    visited[source] = 2
    return False


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        graph = [[] for i in range(N)]
        for i in range(M):
            u, v = map(int, input().split())
            graph[u - 1].append(v - 1)
        is_cycle = False
        visited = [0 for i in range(N)]
        for i in range(N):
            if visited[i] != 2:
                is_cycle = dfs(i, graph, visited)
                if is_cycle:
                    break
        print("YES" if is_cycle else "NO")
