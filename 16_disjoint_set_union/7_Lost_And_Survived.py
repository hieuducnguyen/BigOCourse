"""
Link: https://www.spoj.com/problems/LOSTNSURVIVED/
Time complexity: O(Q * Log(N) + N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq


class Union_Find:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
        self.max = 1
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
        if self.size[root_u] > self.size[root_v]:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        elif self.size[root_v] > self.size[root_u]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        self.max = max(self.max, self.size[root_u], self.size[root_v])
        return True


if __name__ == '__main__':
    N, Q = map(int, input().split())
    union_find = Union_Find(N)
    min_heap = [(1, i) for i in range(N)]
    for q in range(Q):
        A, B = map(lambda x: int(x) - 1, input().split())
        union_find.union(A, B)
        root_A = union_find.find(A)
        heapq.heappush(min_heap, (union_find.size[root_A], root_A))
        while True:
            if min_heap:
                if union_find.parent[min_heap[0][1]] != min_heap[0][1]:
                    heapq.heappop(min_heap)
                    continue
                if min_heap[0][0] != union_find.size[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                    continue
            break
        if union_find.component == 1:
            print(0)
        else:
            print(union_find.max - min_heap[0][0])
