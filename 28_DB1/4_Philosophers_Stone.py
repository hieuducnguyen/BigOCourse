"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 19/01/2022
"""
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        H, W = map(int, input().split())
        matrix = [[0] * (W + 2)]
        for i in range(H):
            tmp_row = [0]
            tmp_row.extend(list(map(int, input().split())))
            tmp_row.append(0)
            matrix.append(tmp_row)
        max_val = 0
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                matrix[i][j] = max(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1]) + matrix[i][j]
                if i == H:
                    max_val = max(matrix[i][j], max_val)
        print(max_val)
