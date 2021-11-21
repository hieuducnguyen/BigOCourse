"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1594
Time complexity: O(T * R * C)
Space complexity: O(T * R * C)
Author: Nguyen Duc Hieu
"""
from collections import deque

direct_col = [-1, 1, 0, 0]
direct_row = [0, 0, -1, 1]


def bfs(start_row, start_col, end_row, end_col, graph, R, C):
    queue = deque([(start_row, start_col)])
    graph[start_row][start_col] = 1
    while queue:
        source_row, source_col = queue.popleft()
        if source_row == end_row and source_col == end_col:
            break
        for i in range(4):
            next_row = source_row + direct_row[i]
            next_col = source_col + direct_col[i]
            if 0 <= next_col < C and 0 <= next_row < R and graph[next_row][next_col] == 0:
                queue.append((next_row, next_col))
                graph[next_row][next_col] = graph[source_row][source_col] + 1
    return graph[end_row][end_col] - 1


if __name__ == '__main__':
    while True:
        R, C = map(int, input().split())
        if R == 0 and C == 0:
            break
        graph = [[0] * C for i in range(R)]
        row_bomb_num = int(input())
        for i in range(row_bomb_num):
            cols = list(map(int, input().split()))
            row_id = cols.pop(0)
            num_bomb = cols.pop(0)
            for k in cols:
                graph[row_id][k] = -1
        start_row, start_col = map(int, input().split())
        end_row, end_col = map(int, input().split())
        print(bfs(start_row, start_col, end_row, end_col, graph, R, C))
