"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1549
Time complexity: O(T * (N + M * Log(N)))
Space complexity: O(T * N)
Author: Nguyen Duc Hieu
"""


class Union_Find:
    def __init__(self, N):
        self.component = N
        self.rank = [1] * N
        self.parent = [i for i in range(N)]

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
            self.rank[root_u] += self.rank[root_v]
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
            self.rank[root_v] += self.rank[root_u]
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += self.rank[root_u]


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N, M = map(int, input().split())
        union_find = Union_Find(N)
        for m in range(M):
            A, B = map(int, input().split())
            union_find.union(A - 1, B - 1)
        max_friend = 1
        for i in range(N):
            if union_find.parent[i] == i and union_find.rank[i] > max_friend:
                max_friend = union_find.rank[i]
        print(max_friend)
