"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 11/12/2021
"""
from collections import deque

if __name__ == '__main__':
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    graph = [[] for _ in range(26)]
    indegrees = [0] * 26
    for first, second in zip(words, words[1:]):
        for c, d in zip(first, second):
            if c != d:
                graph[ord(c) - ord('a')].append(ord(d) - ord('a'))
                indegrees[ord(d) - ord('a')] += 1
                break
        else:
            if len(first) >= len(second):
                print("Impossible")
                exit()
    queue = deque(x for x in range(26) if indegrees[x] == 0)
    orderings = []
    while queue:
        src = queue.popleft()
        orderings.append(chr(src + ord('a')))
        for adjacency in graph[src]:
            indegrees[adjacency] -= 1
            if indegrees[adjacency] == 0:
                queue.append(adjacency)
    if len(orderings) == 26:
        print(*orderings, sep="")
    else:
        print("Impossible")
