"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 28/12/2021
"""


def printBoard(board, N):
    for i in range(N):
        print(*board[i], sep=" ")
    print()


def check(board, row, col, N):
    for i in range(N):
        if board[i][col]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    return True


def NQueen(board, row, N):
    if row == N:
        printBoard(board, N)
        return
    for col in range(N):
        if check(board, row, col, N):
            board[row][col] = 1
            NQueen(board, row + 1, N)
            board[row][col] = 0


if __name__ == '__main__':
    N = 4
    board = [[0] * N for _ in range(N)]
    NQueen(board, 0, N)
