"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 11/12/2021
"""
import heapq

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, R = map(int, input().split())
        graph = [[] for _ in range(N)]
        indegrees = [0] * N
        for r in range(R):
            a, b = map(int, input().split())
            graph[b].append(a)
            indegrees[a] += 1
        min_heap = []
        for n in range(N):
            if indegrees[n] == 0:
                heapq.heappush(min_heap, (1, n))
        orderings = []
        while min_heap:
            src = heapq.heappop(min_heap)
            orderings.append(src)
            for adjacency in graph[src[1]]:
                indegrees[adjacency] -= 1
                if indegrees[adjacency] == 0:
                    heapq.heappush(min_heap, (src[0] + 1, adjacency))
        print("Scenario #{}:".format(t + 1))
        for item in orderings:
            print(item[0], item[1])
