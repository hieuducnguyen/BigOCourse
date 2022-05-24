"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 19/01/2022
"""
if __name__ == '__main__':
    m, n = map(int, input().split())
    matrix = []
    exist_1 = False
    for i in range(m):
        matrix.append(list(map(int, input().split())))
        if not exist_1 and sum(matrix[-1]) != 0:
            exist_1 = True
    row_list = []
    col_list = []
    for i in range(m):
        num_1 = 0
        for j in range(n):
            if matrix[i][j] == 1:
                num_1 += 1
        if num_1 == n:
            row_list.append(i)
    for i in range(n):
        num_1 = 0
        for j in range(m):
            if matrix[j][i] == 1:
                num_1 += 1
        if num_1 == m:
            col_list.append(i)
    if (len(row_list) > 0 and len(col_list) == 0) or (len(row_list) == 0 and len(col_list) > 0):
        print("NO")
        exit()
    transform_matrix = [[0] * n for _ in range(m)]
    if len(row_list) == len(col_list) == 0:
        if exist_1:
            print("NO")
            exit()
        print("YES")
        for i in range(m):
            print(*transform_matrix[i], sep=" ")
        exit()
    first_row = row_list[0]
    first_col = col_list[0]
    result = set()
    for row in row_list:
        result.add((row, first_col))
    for col in col_list[1:]:
        result.add((first_row, col))
    for x, y in result:
        for i in range(m):
            transform_matrix[i][y] = 1
        for j in range(n):
            transform_matrix[x][j] = 1
    for i in range(m):
        for j in range(n):
            if transform_matrix[i][j] != matrix[i][j]:
                print("NO")
                exit()
    print("YES")
    result_matrix = [[0] * n for _ in range(m)]
    for i, j in result:
        result_matrix[i][j] = 1
    for i in range(m):
        print(*result_matrix[i], sep=" ")
