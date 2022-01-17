"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 02/01/2022
"""
import copy

import math

INF = int(1e10)


def cal(tmp_result, num_list):
    return abs(num_list[tmp_result[0]] / num_list[tmp_result[1]] - num_list[tmp_result[2]] / num_list[tmp_result[3]])


def min_diff(num_list, N, tmp_result, result):
    if N == 0:
        min_cost = cal(result[-1], num_list) if result else INF
        tmp_min = cal(tmp_result, num_list)
        if math.isclose(min_cost, tmp_min) or tmp_min > min_cost:
            return
        result.clear()
        result.append(copy.deepcopy(tmp_result))
        return
    for i in range(len(num_list)):
        if i not in tmp_result:
            tmp_result.append(i)
            min_diff(num_list, N - 1, tmp_result, result)
            tmp_result.pop()


if __name__ == '__main__':
    num_list = list(map(int, input().split()))
    tmp_result = []
    result = []
    min_diff(num_list, 4, tmp_result, result)
    print(*result[-1], sep=" ")
