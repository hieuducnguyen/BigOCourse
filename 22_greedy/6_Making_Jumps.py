"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 05/01/2022
"""
import sys

sys.setrecursionlimit(10 ** 4)

direct_X = [-2, -2, -1, -1, 1, 1, 2, 2]
direct_Y = [-1, 1, -2, 2, -2, 2, -1, 1]


def valid_pos(row, col, num_row, pos):
    return 0 <= row < num_row and pos[row][0] <= col < pos[row][1]


def count_horse(pos, row, col, num_row, tmp_result, result):
    for i in range(8):
        new_row = row + direct_X[i]
        new_col = col + direct_Y[i]
        index = new_row * 10 + new_col
        if index in tmp_result:
            continue
        if valid_pos(new_row, new_col, num_row, pos):
            tmp_result.append(index)
            count_horse(pos, new_row, new_col, num_row, tmp_result, result)
            tmp_result.pop()
    result.add(len(tmp_result))


if __name__ == '__main__':
    tc = 0
    while True:
        num_row, *input_list, = map(int, input().split())
        if num_row == 0:
            break
        pos = []
        num_possible_pos = 0
        for i in range(0, num_row * 2, 2):
            pos.append((input_list[i], input_list[i] + input_list[i + 1]))
            num_possible_pos += input_list[i + 1]
        # print(pos)
        tmp_result = [pos[0][0]]
        result = set()
        result.add(1)
        count_horse(pos, 0, pos[0][0], num_row, tmp_result, result)
        real_possible = max(result)
        tc += 1
        un_reach = (num_possible_pos - real_possible)
        print("Case {}, {} square{} can not be reached.".format(tc, un_reach, "s" if un_reach != 1 else ""))
