"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 10/12/2021
"""
from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split())
    graph = [[] for _ in range(N)]
    indegrees = [0] * N
    for i in range(K):
        num, *adjacency_list = map(lambda x: int(x) - 1, input().split())
        for adjacency in adjacency_list:
            graph[i].append(adjacency)
            indegrees[adjacency] += 1
    queue = deque(i for i in range(N) if indegrees[i] == 0)
    orderings = []
    while queue:
        src = queue.popleft()
        orderings.append(src)
        for adjacency in graph[src]:
            indegrees[adjacency] -= 1
            if indegrees[adjacency] == 0:
                queue.append(adjacency)
    i = 0
    member_list = []
    for item in orderings:
        member_list.append((item + 1, i))
        i = item + 1
    member_list.sort()
    for item in member_list:
        print(item[1])
