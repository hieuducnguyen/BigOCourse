"""
Link:
Time complexity: O(Q* (N + N -1 ))
Space complexity: O(N + N - 1)
"""

from collections import deque


def bfs(graph, source, dest):
    queue = deque()
    visited = [False] * len(graph)
    visited[source] = True
    queue.append((source, 0))
    while queue:
        source = queue.popleft()
        if source[0] == dest:
            return source[1]
        for adjacency in graph[source[0]]:
            if not visited[adjacency]:
                visited[adjacency] = True
                queue.append((adjacency, source[1] + 1))
    return 10000


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    Q = int(input())
    friend_list = []
    for _ in range(Q):
        friend_list.append(int(input()) - 1)
    distance = []
    for friend_id in range(Q):
        distance.append(bfs(graph, 0, friend_list[friend_id]))
    min_id = friend_list[0]
    min_distance = distance[0]
    for i in range(1, Q):
        if distance[i] < min_distance or distance[i] == min_distance and friend_list[i] < min_id:
            min_distance = distance[i]
            min_id = friend_list[i]

    print(min_id + 1)
