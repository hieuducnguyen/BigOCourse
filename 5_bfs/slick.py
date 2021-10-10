"""
Link:
Time complexity: O(N * M)
Space complexity: O(N * M)
"""

from queue import Queue

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(N, M, graph, visited, start_x, start_y):
    visited[start_y][start_x] = True
    q = Queue()
    q.put((start_x, start_y))
    size = 1
    while q.qsize() != 0:
        point = q.get()
        for direct in directions:
            adjacency_x = direct[0] + point[0]
            adjacency_y = direct[1] + point[1]
            if 0 <= adjacency_x < M and 0 <= adjacency_y < N and not visited[adjacency_y][adjacency_x] and \
                    graph[adjacency_y][adjacency_x] == 1:
                size += 1
                visited[adjacency_y][adjacency_x] = True
                q.put((adjacency_x, adjacency_y))
    return size


def count_slick(N, M, graph):
    slick_dict = {}
    visited = [[False for t in range(M)] for v in range(N)]
    for i in range(M):
        for j in range(N):
            if not visited[j][i] and graph[j][i] == 1:
                size = bfs(N, M, graph, visited, i, j)
                slick_dict[size] = slick_dict.get(size, 0) + 1
    total_size = sum(map(lambda x: x[1], slick_dict.items()))
    print(total_size)
    slick_dict = sorted(slick_dict.items(), key=lambda x: x[0])
    for item in slick_dict:
        print(item[0], item[1])


if __name__ == '__main__':
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        graph = []
        for _ in range(N):
            graph.append(list(map(int, input().split())))
        count_slick(N, M, graph)
