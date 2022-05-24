"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 19/01/2022
"""
import copy
import sys

sys.setrecursionlimit(10 * 4)


def count(N, K, pos, result, tmp_result):
    if pos == N:
        result.append(copy.deepcopy(tmp_result))
        return
    start = 0 if pos != 0 else 1
    for i in range(start, K):
        if len(tmp_result) > 0 and i == tmp_result[-1] == 0:
            continue
        tmp_result.append(i)
        count(N, K, pos + 1, result, tmp_result)
        tmp_result.pop()


def check_valid(bin_val):
    pre_val = False
    for val in bin_val:
        if val == 1:
            if pre_val:
                return False
            pre_val = True
        else:
            pre_val = False
    return True


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    remain = 0
    for i in range(2 ** (N - 1)):
        bin_val = list(map(int, list(str(bin(i)))[2:]))
        # print(bin_val)
        if check_valid(bin_val):
            num_0 = sum(bin_val)
            remain += (K - 1) ** (N - 1 - num_0)
    result = remain * (K - 1)
    print(result)
# result = []
# tmp_result = []
# count(N, K, 0, result, tmp_result)
# print(len(result))
# result = (K - 1) * K ** (N - 1)
# wrong_total = 0
# for i in range(2, N):
#     if N - 1 - i == 0:
#         tmp_wrong = 1
#     else:
#         val = (N - i)
#         tmp_wrong = val * (K - 1) ** (N - 1 - i)
#     wrong_total += tmp_wrong
# result -= wrong_total
# print(result)
