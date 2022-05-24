"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 04/02/2022
"""
from collections import deque


class Train:
    def __init__(self, start_time_str, end_time_str, id, source):
        hour_start, minute_start = map(int, start_time_str.split(":"))
        self.start_time = hour_start * 60 + minute_start
        hour_end, minute_end = map(int, end_time_str.split(":"))
        self.end_time = hour_end * 60 + minute_end
        self.id = id
        self.source = source

    def __str__(self):
        return "Train(id={}, start={}, end={})".format(self.id, self.start_time, self.end_time)

    def __lt__(self, other):
        return self.start_time < other.start_time


def dfs(src_train, graph, indegree, queue, visited, train_map):
    visited[src_train.id] = True
    if graph[src_train.id]:
        adjacency_next = -1
        END_INF = int(2e3)
        for adjacency_id in graph[src_train.id]:
            adjacency = train_map.get(adjacency_id)
            if not visited[adjacency.id] and adjacency.end_time < END_INF:
                END_INF = adjacency.end_time
                adjacency_next = adjacency.id
            indegree[adjacency.id] -= 1
            if indegree[adjacency.id] == 0:
                queue.append(adjacency)
        if adjacency_next != -1:
            return dfs(train_map.get(adjacency_next), graph, indegree, queue, visited, train_map)


if __name__ == '__main__':
    N = int(input())
    for n in range(N):
        T = int(input())
        A, B = map(int, input().split())
        A_list_train = []
        B_list_train = []
        train_map = {}
        id = 0
        for a in range(A):
            start_time, end_time = input().split()
            train = Train(start_time, end_time, id, 0)
            A_list_train.append(train)
            train_map[id] = train
            id += 1
        for b in range(B):
            start_time, end_time = input().split()
            train = Train(start_time, end_time, id, 1)
            B_list_train.append(train)
            train_map[id] = train
            id += 1
        indegree = [0] * id
        graph = [[] for _ in range(id)]
        for train_a in A_list_train:
            for train_b in B_list_train:
                if train_a.end_time + T <= train_b.start_time:
                    graph[train_a.id].append(train_b.id)
                    indegree[train_b.id] += 1

        for train_b in B_list_train:
            for train_a in A_list_train:
                if train_b.end_time + T <= train_a.start_time:
                    graph[train_b.id].append(train_a.id)
                    indegree[train_a.id] += 1
        queue = deque()
        num_A, num_B = 0, 0
        for i in range(id):
            if indegree[i] == 0:
                queue.append(train_map.get(i))
        visited = [False] * id
        while queue:
            src_train = queue.pop()
            if visited[src_train.id]:
                continue
            if src_train.source == 0:
                num_A += 1
            else:
                num_B += 1
            dfs(src_train, graph, indegree, queue, visited, train_map)
        print("Case #{}: {} {}".format(n + 1, num_A, num_B))
