"""
Link: https://codeforces.com/problemset/problem/217/A
Time complexity: O(N^2 * log(N))
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class Union_Find:
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
            return False
        self.component -= 1
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += 1
        return True


if __name__ == '__main__':
    N = int(input())
    point_list = []
    union_find = Union_Find(N)
    for n in range(N):
        A, B = map(int, input().split())
        point_list.append((A, B))
    for i in range(N):
        for j in range(i + 1, N):
            if point_list[i][0] == point_list[j][0] or point_list[i][1] == point_list[j][1]:
                union_find.union(i, j)
    print(union_find.component - 1)
