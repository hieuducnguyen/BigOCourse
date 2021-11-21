"""
Link: https://codeforces.com/problemset/problem/104/C
Time complexity: O(M * Log(N) + N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class Union_Find:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1] * N
        self.component = N

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        self.component -= 1
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
            self.rank[root_u] += self.rank[root_v]
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
            self.rank[root_v] += self.rank[root_u]
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += self.rank[root_u]
        return True


if __name__ == '__main__':
    N, M = map(int, input().split())
    union_find = Union_Find(N)
    num_cycle = 0
    for m in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        if not union_find.union(a, b):
            num_cycle += 1
    if num_cycle == 1 and union_find.component == 1:
        print("FHTAGN!")
        exit()
    print("NO")
