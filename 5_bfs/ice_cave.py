"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

from queue import Queue

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(start_r, start_c, end_r, end_c, graph, n, m):
    q = Queue()
    q.put((start_r, start_c))
    while q.qsize() != 0:
        point = q.get()
        for direct in directions:
            next_r = point[0] + direct[0]
            next_c = point[1] + direct[1]
            if 0 > next_r or next_r >= n or next_c < 0 or next_c >= m:
                continue
            if graph[next_r][next_c] == 'X' and next_r == end_r and next_c == end_c:
                return True
            if graph[next_r][next_c] == '.':
                graph[next_r][next_c] = 'X'
                q.put((next_r, next_c))
    return False


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(input()))
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    if bfs(start_r - 1, start_c - 1, end_r - 1, end_c - 1, graph, n, m):
        print('YES')
    else:
        print('NO')
