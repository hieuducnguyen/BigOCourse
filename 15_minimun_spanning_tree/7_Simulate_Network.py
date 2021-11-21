"""
Link: Hackerearth
Time complexity: O(M * Log(N) + N + Q * Log(N))
Space complexity: O(M + N)
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


"""Prim"""


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


def method_prim():
    global entry
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


"""Union Find support Kruskal"""


class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += 1
        return True


"""Kruskal"""


def kruskal(edge_list, N):
    MST_edge_list = []
    union_find = UnionFind(N)
    edge_list.sort(key=lambda x: x[2])
    for source, dest, weight in edge_list:
        if union_find.union(source, dest):
            MST_edge_list.append(Entry(weight, source, dest))
    return MST_edge_list


def method_kruskal():
    N, M = map(int, input().split())
    edge_list = []
    for m in range(M):
        A, B, L = map(int, input().split())
        edge_list.append((A - 1, B - 1, L))
    MST_edge_list = kruskal(edge_list, N)
    heapq.heapify(MST_edge_list)
    Q = int(input())
    replace_cables_min_heap = list(map(int, input().split()))
    heapq.heapify(replace_cables_min_heap)
    while replace_cables_min_heap and replace_cables_min_heap[0] < MST_edge_list[0].weight:
        min_cable = heapq.heappop(replace_cables_min_heap)
        max_weight_entry = heapq.heappop(MST_edge_list)
        max_weight_entry.weight = min_cable
        heapq.heappush(MST_edge_list, max_weight_entry)
    print(sum(list(map(lambda x: x.weight, MST_edge_list))))


if __name__ == '__main__':
    # method_prim()
    method_kruskal()
