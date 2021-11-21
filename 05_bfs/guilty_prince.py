"""
Link:
Time complexity: O(W * H + W * H)
Space complexity: O(W * H)
"""

from queue import Queue

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(W, H, graph, start_x, start_y):
    point = (start_x, start_y)
    visited = [[False for _ in range(H)] for _ in range(W)]
    num_visited = 1
    q = Queue()
    visited[point[0]][point[1]] = True
    q.put(point)
    while q.qsize() != 0:
        point = q.get()
        for direc in directions:
            new_x = point[0] + direc[0]
            new_y = point[1] + direc[1]
            if 0 <= new_x < W and 0 <= new_y < H:
                if not visited[new_x][new_y] and graph[new_x][new_y] == '.':
                    visited[new_x][new_y] = True
                    num_visited += 1
                    q.put((new_x, new_y))
    return num_visited


if __name__ == '__main__':
    test_cast = int(input())
    for _ in range(test_cast):
        X, Y = map(int, input().split())
        graph = []
        start_x, start_y = -1, -1
        for i in range(Y):
            text = input()
            if '@' in text:
                start_x, start_y = i, text.index('@')
            graph.append(list(text))
        print("Case %s: %s" % (_ + 1, bfs(Y, X, graph, start_x, start_y)))
