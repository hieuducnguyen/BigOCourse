"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


class Entry:
    def __init__(self, weight, source=None, dest=None):
        self.weight = weight
        self.source = source
        self.dest = dest

    def __lt__(self, other):
        return self.weight > other.weight


def prim(graph, N):
    path = [-1] * N
    dist = [INF] * N
    visited = [False] * N
    min_heap = [(0, 0)]
    dist[0] = 0
    while min_heap:
        cur_w, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                dist[adjacency] = weight
                path[adjacency] = source
                heapq.heappush(min_heap, (dist[adjacency], adjacency))
    return path, dist


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for m in range(M):
        A, B, L = map(int, input().split())
        graph[A - 1].append((B - 1, L))
        graph[B - 1].append((A - 1, L))
    path, dist = prim(graph, N)
    max_heap = []
    for i in range(N):
        if path[i] != -1:
            max_heap.append(Entry(dist[i], path[i], i))
    heapq.heapify(max_heap)

    Q = int(input())
    replace_min_heap = list(map(int, input().split()))
    heapq.heapify(replace_min_heap)

    while len(replace_min_heap) > 0 and replace_min_heap[0] < max_heap[0].weight:
        entry = heapq.heappop(max_heap)
        min_replace = heapq.heappop(replace_min_heap)
        entry.weight = min_replace
        heapq.heappush(max_heap, entry)
    print(sum(list(map(lambda x: x.weight, max_heap))))
