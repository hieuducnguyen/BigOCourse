"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
from collections import deque


def bfs(graph, source):
    visited = [-1 for i in range(len(graph))]
    queue = deque()
    visited[source] = 0
    queue.append(source)
    while queue:
        source = queue.popleft()
        for adjacency in graph[source]:
            if visited[adjacency] < 0:
                visited[adjacency] = visited[source] + 1
                queue.append(adjacency)
    return visited


if __name__ == '__main__':
    N = int(input())
    graph = [[] for i in range(N * 3)]
    map_name_id = {}
    map_id_name = {}
    index_friend = -1
    for i in range(N):
        team_mate = list(input().split())
        for friend in team_mate:
            if friend not in map_name_id:
                index_friend += 1
                map_name_id[friend] = index_friend
                map_id_name[index_friend] = friend
        for u in range(3):
            for v in range(u + 1, 3):
                graph[map_name_id[team_mate[u]]].append(map_name_id[team_mate[v]])
                graph[map_name_id[team_mate[v]]].append(map_name_id[team_mate[u]])
    if "Isenbaev" in map_name_id:
        dist = bfs(graph, map_name_id["Isenbaev"])
    else:
        dist = [-1 for i in range(len(graph))]
    friend_name_order_list = sorted(map_name_id.keys())
    for name in friend_name_order_list:
        distance = dist[map_name_id[name]] if dist[map_name_id[name]] >= 0 else "undefined"
        print("{} {}".format(name, distance))
