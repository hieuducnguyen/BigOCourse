"""
Link: https://codeforces.com/problemset/problem/468/B
Time complexity: O(N * Log(N))
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
        if root_v == root_u:
            return False
        self.component -= 1
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.parent[root_v] > self.parent[root_u]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += 1
        return True


def method_1():
    global values
    N, A, B = map(int, input().split())
    values = list(map(int, input().split()))
    map = dict()
    union_find = Union_Find(N + 2)
    for i in range(len(values)):
        map[values[i]] = i
    for k in range(2):
        for val in values:
            if map.get(val, -1) > -1:
                if map.get(A - val, -1) > -1 >= map.get(B - val, -1):
                    union_find.union(N, map[val])
                    union_find.union(N, map[A - val])
                    map[val] = -1
                    map[A - val] = -1
                elif map.get(A - val, -1) <= -1 < map.get(B - val, -1):
                    union_find.union(N + 1, map[val])
                    union_find.union(N + 1, map[B - val])
                    map[val] = -1
                    map[B - val] = -1
                else:
                    if -1 >= map.get(A - val, -1) and -1 >= map.get(B - val, -1):
                        print("NO")
                        exit()
    print("YES")
    root_0 = union_find.find(N)
    root_1 = union_find.find(N + 1)
    for i in range(len(values)):
        if union_find.find(i) == root_0:
            print("0", end=" ")
        else:
            print("1", end=" ")


def method_2():
    N, A, B = map(int, input().split())
    values = list(map(int, input().split()))
    map_index = dict()
    for i in range(N):
        val = values[i]
        map_index[val] = i
        if val >= max(A, B):
            print("NO")
            exit()
    union_find = Union_Find(N + 2)
    for val in values:
        if (A - val) in map_index:
            union_find.union(map_index[val], map_index[A - val])
        else:
            union_find.union(N + 1, map_index[val])
        if (B - val) in map_index:
            union_find.union(map_index[val], map_index[B - val])
        else:
            union_find.union(N, map_index[val])
    root_A = union_find.find(N)
    root_B = union_find.find(N + 1)
    if root_A == root_B:
        print("NO")
        exit()
    print("YES")
    for i in range(N):
        if union_find.find(i) == root_A:
            print("0", end=" ")
        else:
            print("1", end=" ")


if __name__ == '__main__':
    # method_1()
    method_2()
