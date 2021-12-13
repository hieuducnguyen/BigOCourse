"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 11/12/2021
"""
from collections import defaultdict, deque

INF = int(10 ** 9) - 1
direct_x = [-1, -1, -1, 0, 0, 1, 1, 1]
direct_y = [1, 0, -1, 1, -1, 1, 0, -1]

if __name__ == '__main__':
    graph = defaultdict(set)
    x_start, y_start, x_dest, y_dest = map(lambda x: int(x) - 1, input().split())
    graph[x_start].add(y_start)
    graph[x_dest].add(y_dest)
    N = int(input())
    for i in range(N):
        r, a, b = map(lambda x: int(x) - 1, input().split())
        for k in range(a, b + 1):
            graph[r].add(k)
    visited = defaultdict(dict)
    queue = deque([(x_start, y_start)])
    visited[x_start][y_start] = 0
    distance = -1
    while queue:
        x_src, y_src = queue.popleft()
        if x_src == x_dest and y_src == y_dest:
            distance = visited.get(x_dest).get(y_dest)
            break
        for i in range(8):
            new_x = x_src + direct_x[i]
            new_y = y_src + direct_y[i]
            if new_x >= 0 and new_y <= INF and graph[new_x].__contains__(new_y) and (
                    new_x not in visited or new_y not in visited[new_x]):
                queue.append((new_x, new_y))
                visited[new_x][new_y] = visited[x_src][y_src] + 1
    print(distance)
