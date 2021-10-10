"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

from queue import Queue

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(r, c, graph, visited, N, M):
    s, w = 0, 0
    if graph[r][c] == 'k':
        s = 1
    elif graph[r][c] == 'v':
        w = 1
    q = Queue()
    q.put((r, c))
    visited[r][c] = True
    join = True
    while q.qsize() != 0:
        point = q.get()
        for direct in directions:
            next_r = point[0] + direct[0]
            next_c = point[1] + direct[1]
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M or visited[next_r][next_c]:
                continue
            if graph[next_r][next_c] != '#':
                if next_r == 0 or next_c == 0 or next_r == N - 1 or next_c == M - 1:
                    join = False
                if graph[next_r][next_c] == 'k':
                    s += 1
                elif graph[next_r][next_c] == 'v':
                    w += 1
                visited[next_r][next_c] = True
                q.put((next_r, next_c))

    if not join:
        return (s, w)
    else:
        if s > w:
            return (s, 0)
        else:
            return (0, w)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = []
    for i in range(N):
        graph.append(list(input()))
    visited = [[False for i in range(M)] for j in range(N)]
    sheep, wolf = 0, 0
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and graph[r][c] != '#':
                v, k = bfs(r, c, graph, visited, N, M)
                sheep += v
                wolf += k
    print('%s %s' % (sheep, wolf))
