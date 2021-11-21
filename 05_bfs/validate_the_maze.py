"""
Link: https://www.spoj.com/problems/MAKEMAZE/
Time complexity: O(M * N + M + N)
Space complexity: O(M * N)
M: row
N: col
M * N for find start point and end point
M + N for bfs
"""

from queue import Queue

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(start_point, end_point, graph, M, N):
    visited = [[False for _ in range(N)] for _ in range(M)]
    q = Queue()
    visited[start_point[0]][start_point[1]] = True
    q.put(start_point)
    while q.qsize() != 0:
        point = q.get()
        for direct in directions:
            next_point = (point[0] + direct[0], point[1] + direct[1])
            if M > next_point[0] >= 0 and N > next_point[1] >= 0:
                if graph[next_point[0]][next_point[1]] == '.':
                    if next_point[0] == end_point[0] and next_point[1] == end_point[1]:
                        return True
                    if not visited[next_point[0]][next_point[1]]:
                        visited[next_point[0]][next_point[1]] = True
                        q.put((next_point[0], next_point[1]))
    return False


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        M, N = map(int, input().split())
        end_point = []
        graph = []
        for r in range(M):
            graph.append(list(input()))
        for i in range(M):
            for j in range(len(graph[i])):
                if graph[i][j] == '.' and (i == 0 or i == M - 1 or j == 0 or j == N - 1):
                    end_point.append((i, j))
        if len(end_point) == 2:
            valid = bfs(end_point[0], end_point[1], graph, M, N)
        else:
            valid = False
        if valid:
            print("valid")
        else:
            print("invalid")
