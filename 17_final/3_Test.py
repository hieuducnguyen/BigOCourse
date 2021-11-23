"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.component = N

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        self.component -= 1
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += 1
        return


if __name__ == '__main__':
    test_case = 1
    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break
        union_find = UnionFind(N)
        for m in range(M):
            u, v = map(lambda x: int(x) - 1, input().split())
            union_find.union(u, v)
        print("Case {}: {}".format(test_case, union_find.component))
        test_case += 1
