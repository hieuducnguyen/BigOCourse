"""
Link: https://www.spoj.com/problems/MST/
Time complexity: O(M * Log(N))
Space complexity: O(M + N)
Author: Nguyen Duc Hieu
"""
import heapq

INF = int(1e10)


def prim():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for m in range(M):
        i, j, k = map(int, input().split())
        graph[i - 1].append((j - 1, k))
        graph[j - 1].append((i - 1, k))
    visited = [False] * N
    dist = [INF] * N
    dist[0] = 0
    min_heap = [(0, 0)]
    while min_heap:
        weight_source, source = heapq.heappop(min_heap)
        if visited[source]: continue
        visited[source] = True
        for adjacency, weight in graph[source]:
            if not visited[adjacency] and dist[adjacency] > weight:
                heapq.heappush(min_heap, (weight, adjacency))
                dist[adjacency] = weight
    return sum(dist)


class Union_Find:
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


def kruskal():
    N, M = map(int, input().split())
    edge_list = []
    union_find = Union_Find(N)
    for m in range(M):
        A, B, W = map(int, input().split())
        edge_list.append((A - 1, B - 1, W))
    sorted_edge_list = sorted(edge_list, key=lambda x: x[2])
    weight = 0
    for x, y, w in sorted_edge_list:
        if union_find.union(x, y):
            weight += w
    return weight


if __name__ == '__main__':
    # MST_dist = prim()
    # print(MST_dist)
    MST_dist = kruskal()
    print(MST_dist)
