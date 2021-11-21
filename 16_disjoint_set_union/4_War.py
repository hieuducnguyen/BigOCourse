"""
Link: https://vjudge.net/problem/UVA-10158
Time complexity: O(M * Log(N)) M: num operations
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class Union_Find:
    def __init__(self, size_set):
        self.parent = [i for i in range(size_set)]
        self.rank = [0] * size_set

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += 1


if __name__ == '__main__':
    N = int(input())
    union_find = Union_Find(N * 2)
    while True:
        C, X, Y = map(int, input().split())
        if C == 0:
            break
        if C == 1:
            if union_find.find(X) == union_find.find(Y + N):
                print(-1)
            else:
                union_find.union(X, Y)
                union_find.union(X + N, Y + N)
        elif C == 2:
            if union_find.find(X) == union_find.find(Y):
                print(-1)
            else:
                union_find.union(X, Y + N)
                union_find.union(X + N, Y)
        elif C == 3:
            if union_find.find(X) == union_find.find(Y):
                print(1)
            else:
                print(0)
        else:
            if union_find.find(X) == union_find.find(Y + N):
                print(1)
            else:
                print(0)
