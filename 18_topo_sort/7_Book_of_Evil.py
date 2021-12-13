"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 11/12/2021
"""
from collections import deque


def bfs(start, graph, N, damages, D):
    visited = [-1] * N
    visited[start] = 0
    queue = deque([start])
    while queue:
        src = queue.popleft()
        for adjacency in graph[src]:
            if visited[adjacency] < 0:
                visited[adjacency] = visited[src] + 1
                if visited[adjacency] < D:
                    queue.append(adjacency)
    max_distance = 0
    max_distance_index = start
    for i in damages:
        if max_distance < visited[i]:
            max_distance_index = i
            max_distance = visited[i]
    return max_distance_index, visited


if __name__ == '__main__':
    N, M, D = map(int, input().split())
    if M == 0:
        print(0)
        exit()
    damages = list(map(lambda x: int(x) - 1, input().split()))
    graph = [[] for _ in range(N)]
    for n in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    start_damage_point = damages[0]
    first_point, dist = bfs(start_damage_point, graph, N, damages, 10 ** 9)
    second_point, dist_from_first = bfs(first_point, graph, N, damages, 10 ** 9)
    point, dist_from_second = bfs(second_point, graph, N, damages, D)
    result = 0
    for i in range(N):
        if dist_from_first[i] != -1 and dist_from_first[i] <= D and dist_from_second[i] != -1 and dist_from_second[
            i] <= D:
            result += 1
    print(result)
