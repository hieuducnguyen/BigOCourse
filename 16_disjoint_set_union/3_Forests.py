"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1168
Time complexity: O(TestCase * P^2 * (T + log(P)))
Space complexity: O(TestCase * (P * T + P))
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
    test_case = int(input())
    for tc in range(test_case):
        if tc == 0:
            input()
        P, T = map(int, input().split())
        trees = [set() for _ in range(P)]
        while True:
            try:
                input_text = input()
                if input_text != "":
                    A, B = map(lambda x: int(x) - 1, input_text.split())
                    trees[A].add(B)
                else:
                    break
            except EOFError as e:
                break
        union_find = Union_Find(P)
        for i in range(P):
            for j in range(i + 1, P):
                if trees[i] == trees[j]:
                    union_find.union(i, j)
        print(union_find.component)
        print()
