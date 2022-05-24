"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 03/02/2022
"""
from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    # print(matrix)
    main_diagonal = defaultdict(int)
    second_diagonal = defaultdict(int)
    exist_main_diagonal = defaultdict(int)
    exist_second_diagonal = defaultdict(int)
    for i in range(N):
        for j in range(N):
            main_diagonal[i - j] = main_diagonal[i - j] + matrix[i][j]
            second_diagonal[i + j] = second_diagonal[i + j] + matrix[i][j]
    max_even, x_even, y_even = -1, -1, -1
    max_odd, x_odd, y_odd = -1, -1, -1
    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 0:
                if main_diagonal[i - j] + second_diagonal[i + j] - matrix[i][j] > max_even:
                    max_even = main_diagonal[i - j] + second_diagonal[i + j] - matrix[i][j]
                    x_even = i
                    y_even = j
            else:
                if main_diagonal[i - j] + second_diagonal[i + j] - matrix[i][j] > max_odd:
                    max_odd = main_diagonal[i - j] + second_diagonal[i + j] - matrix[i][j]
                    x_odd = i
                    y_odd = j
    print(max_even + max_odd)
    print(x_even + 1, y_even + 1, x_odd + 1, y_odd + 1)
