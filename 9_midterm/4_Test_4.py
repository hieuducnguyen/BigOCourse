"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1594
Time complexity: O(T * R * C)
Space complexity: O(T * R * C)
Author: Nguyen Duc Hieu
"""
from collections import deque

direct_col = [-1, 1, 0, 0]
direct_row = [0, 0, -1, 1]


def bfs(start_x, start_y, end_x, end_y, graph, R, C):
    graph[start_x][start_y] = -1
    distance = [[-1 for i in range(C)] for j in range(R)]
    distance[start_x][start_y] = 0
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        u, v = queue.popleft()
        if u == end_x and v == end_y:
            break
        for direct in range(4):
            new_u = u + direct_row[direct]
            new_v = v + direct_col[direct]
            if 0 <= new_u < R and 0 <= new_v < C and graph[new_u][new_v] != 1 and graph[new_u][new_v] != -1:
                distance[new_u][new_v] = distance[u][v] + 1
                graph[new_u][new_v] = -1
                queue.append((new_u, new_v))
    return distance[end_x][end_y]


if __name__ == '__main__':
    while True:
        R, C = map(int, input().split())
        if R == 0 and C == 0:
            break
        num_row_bomb = int(input())
        graph = [[0 for i in range(C)] for j in range(R)]
        for i in range(num_row_bomb):
            input_list = list(map(int, input().split()))
            index_bomb_row = input_list[0]
            num_bomb_in_row = input_list[1]
            index_collumn = input_list[2:]
            for k in index_collumn:
                graph[index_bomb_row][k] = 1
        start_x, start_y = map(int, input().split())
        end_x, end_y = map(int, input().split())
        time = bfs(start_x, start_y, end_x, end_y, graph, R, C)
        print(time)
