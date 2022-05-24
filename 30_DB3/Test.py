"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 25/01/2022
"""


def LIS_Topdown(num_list, dp, end):
    if dp[end] != -1:
        return dp[end]
    LIS = 1
    for i in range(end):
        if num_list[end] > num_list[i]:
            LIS = max(LIS, LIS_Topdown(num_list, dp, i) + 1)
    dp[end] = LIS
    return LIS


def LIS(num_list, dp, path):
    len_num = len(num_list)
    len_LIS = 1
    for i in range(1, len_num):
        for j in range(i):
            if num_list[i] > num_list[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                path[i] = j
                if len_LIS < dp[i]:
                    len_LIS = dp[i]
                    last = i
    return last


def lower_bound(index_list, key, num_list):
    start = 0
    end = len(index_list)
    result = end
    while start < end:
        mid = (start + end) // 2
        if num_list[index_list[mid]] >= key:
            end = mid
            result = mid
        else:
            start = mid + 1
    return result


def LIS_optimize(num_list, path, dp):
    num_len = len(num_list)
    dp.append(0)
    for i in range(1, num_len):
        if num_list[dp[0]] > num_list[i]:
            path[i] = -1
            dp[0] = i
        elif num_list[dp[-1]] < num_list[i]:
            path[i] = dp[-1]
            dp.append(i)
        else:
            pos = lower_bound(dp, num_list[i], num_list)
            path[i] = dp[pos - 1]
            dp[pos] = i


if __name__ == '__main__':
    # num_list = [2, 5, 12, 3, 10, 6, 8, 14, 4, 11, 7, 15]
    # dp = []
    # path = [-1] * len(num_list)
    # LIS_optimize(num_list, path, dp)
    # last = dp[-1]
    # while last != -1:
    #     print(num_list[last], end=" ")
    #     last = path[last]
    for i in range(1, 62500):
        print(i, end=" ")
# print(len(dp))
# print(dp)

# num_list.sort()
# print(num_list)
# print(lower_bound(num_list, 19))
# last_pos = LIS(num_list, dp, path)
# print(LIS_Topdown(num_list, dp, len(num_list) - 1))
# result = []
# while last_pos != -1:
#     result.append(last_pos)
#     last_pos = path[last_pos]
# result.reverse()
# print(result)
