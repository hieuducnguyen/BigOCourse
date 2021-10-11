"""
Link:
Time complexity: O(T * (N + E))
Space complexity: O(T * (N + E))
"""

from collections import deque


def dfs(graph, person, visited):
    queue = deque()
    visited[person] = True
    queue.append(person)
    while queue:
        source = queue.popleft()
        for adjacency in graph[source]:
            if not visited[adjacency]:
                visited[adjacency] = True
                queue.append(adjacency)


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        E = int(input())
        graph = [[] for _ in range(N)]
        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        meet_person = 0
        visited = [False] * N
        for person in range(N):
            if not visited[person]:
                dfs(graph, person, visited)
                meet_person += 1
        print(meet_person)
