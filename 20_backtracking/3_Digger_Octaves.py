"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 02/01/2022
"""

direct_X = [-1, 0, 0, 1]
direct_Y = [0, 1, -1, 0]


def convert(tmp_result, N):
    tmp_set = list()
    for i in range(8):
        tmp_set.append(tmp_result[i][0] * N + tmp_result[i][1])
    tmp_set.sort()
    return tuple(tmp_set)


def find_route(start_x, start_y, matrix, N, K, tmp_result, result):
    if K == 0:
        tmp_set = convert(tmp_result, N)
        result.add(tmp_set)
        return
    for i in range(4):
        new_x = start_x + direct_X[i]
        new_y = start_y + direct_Y[i]
        if 0 <= new_x <= (N - 1) and 0 <= new_y <= (N - 1) and (new_x, new_y) not in tmp_result and matrix[new_x][
            new_y] != ".":
            tmp_result.append((new_x, new_y))
            find_route(new_x, new_y, matrix, N, K - 1, tmp_result, result)
            tmp_result.pop()


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        matrix = []
        for i in range(N):
            matrix.append(list(input()))
        result = set()
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == ".":
                    continue
                tmp_result = [(i, j)]
                find_route(i, j, matrix, N, 7, tmp_result, result)
        print(len(result))
