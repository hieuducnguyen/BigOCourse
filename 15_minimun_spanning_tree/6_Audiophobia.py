"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&category=116&page=show_problem&problem=989
Time complexity: O(T * (S * Log(C) + Q * C))
Space complexity: O(T * (S + C))
Author: Nguyen Duc Hieu
"""

INF = int(1e10)


def dfs(source, graph, N):
    dist = [INF] * N
    stack = [source]
    dist[source] = 0
    while stack:
        source = stack.pop()
        for adjacency, weight in graph[source]:
            if dist[adjacency] == INF:
                dist[adjacency] = max(dist[source], weight)
                stack.append(adjacency)
    return dist


class Uninon_Find:
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


def kruskal(edge_list, N):
    sorted_edge_list = sorted(edge_list, key=lambda x: x[2])
    MST_grap = [[] for _ in range(N)]
    union_find = Uninon_Find(N)
    for source, dest, weight in sorted_edge_list:
        if union_find.union(source, dest):
            MST_grap[source].append((dest, weight))
            MST_grap[dest].append((source, weight))
    return MST_grap


if __name__ == '__main__':
    test_case = 1
    while True:
        C, S, Q = map(int, input().split())
        if C == 0:
            break
        edge_list = []
        for s in range(S):
            c1, c2, d = map(int, input().split())
            edge_list.append((c1 - 1, c2 - 1, d))
        MST_graph = kruskal(edge_list, C)
        print("Case #{}".format(test_case))
        test_case += 1
        for q in range(Q):
            c1, c2 = map(lambda x: int(x) - 1, input().split())
            dist_from_c1 = dfs(c1, MST_graph, C)
            if dist_from_c1[c2] != INF:
                print(dist_from_c1[c2])
            else:
                print("no path")
        print()
