"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 10/12/2021
"""
import heapq

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    indegrees = [0] * N
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        indegrees[b] += 1
    min_heap = []
    for i in range(N):
        if indegrees[i] == 0:
            heapq.heappush(min_heap, i)
    orderings = []
    while min_heap:
        src = heapq.heappop(min_heap)
        orderings.append(src + 1)
        for adjacency in graph[src]:
            indegrees[adjacency] -= 1
            if indegrees[adjacency] == 0:
                heapq.heappush(min_heap, adjacency)
    if len(orderings) != N:
        print("Sandro fails.")
    else:
        print(*orderings, sep=" ")
