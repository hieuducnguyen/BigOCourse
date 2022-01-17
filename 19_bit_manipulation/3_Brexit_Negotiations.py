"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 14/12/2021
"""
import heapq
from collections import deque


class Event:
    def __init__(self, eventId, time):
        self.eventId = eventId
        self.time = time
        self.max_time = time

    def update_max_time(self, val):
        self.max_time = max(val, self.max_time)

    def __lt__(self, other):
        return self.max_time > other.max_time

    def __str__(self):
        return "Event(id={};time={};sum={})".format(self.eventId, self.time, self.max_time)


def build_total_time(graph, map_event):
    N = len(graph)
    indegrees = [0] * N
    for vertex in range(N):
        for adjacency in graph[vertex]:
            indegrees[adjacency] += 1
    queue = deque()
    for i in range(N):
        if indegrees[i] == 0:
            queue.append(i)
    while queue:
        source = queue.popleft()
        for adjacency in graph[source]:
            map_event[adjacency].update_max_time(map_event[source].max_time)
            indegrees[adjacency] -= 1
            if indegrees[adjacency] == 0:
                queue.append(adjacency)


def min_time(graph, map_event):
    N = len(graph)
    indegrees = [0] * N
    for src in range(N):
        for adjacency in graph[src]:
            indegrees[adjacency] += 1
    max_heap = []
    for i in range(N):
        if indegrees[i] == 0:
            heapq.heappush(max_heap, map_event[i])
    orderings = []
    while max_heap:
        source = heapq.heappop(max_heap)
        orderings.append(source)
        for adjacency in graph[source.eventId]:
            indegrees[adjacency] -= 1
            if indegrees[adjacency] == 0:
                heapq.heappush(max_heap, map_event[adjacency])
    return orderings


if __name__ == '__main__':
    N = int(input())
    graph_from_target = [[] for _ in range(N)]
    graph = [[] for _ in range(N)]
    map_event = dict()
    for i in range(N):
        time, num_event, *pre_event_list = map(lambda x: int(x) - 1, input().split())
        map_event[i] = Event(i, time + 1)
        graph_from_target[i].extend(pre_event_list)
        for pre_event in pre_event_list:
            graph[pre_event].append(i)
    build_total_time(graph_from_target, map_event)
    orderings = min_time(graph, map_event)
    min_longest_time = 0
    for i in range(N):
        event = orderings[i]
        min_longest_time = max(min_longest_time, i + event.time)
    print(min_longest_time)
