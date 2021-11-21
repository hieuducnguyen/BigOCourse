"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=400
Time complexity: O(T * (M log(N) + N))
Space complexity: O(T * N)
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
            return
        self.component -= 1
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += 1


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        if tc == 0:
            input()
        max_vertex = input()
        num_vertex = ord(max_vertex) - ord("A") + 1
        union_find = Union_Find(num_vertex)
        while True:
            try:
                input_edge = input()
                if input_edge == "":
                    break
            except EOFError:
                break
            A, B = map(lambda x: ord(x) - ord("A"), list(input_edge))
            union_find.union(A, B)
        print(union_find.component)
        print()
