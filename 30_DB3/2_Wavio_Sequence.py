"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 26/01/2022
"""


def lower_bound(dp, input_list, key):
    start = 0
    end = len(dp)
    result = end
    while start < end:
        mid = start + (end - start) // 2
        if input_list[dp[mid]] >= key:
            end = mid
            result = mid
        else:
            start = mid + 1
    return result


def LIS(input_list):
    dp = [0]
    len_input = len(input_list)
    LIS_arr = [1]
    for i in range(1, len_input):
        if input_list[dp[0]] > input_list[i]:
            dp[0] = i
        elif input_list[dp[-1]] < input_list[i]:
            dp.append(i)
        else:
            pos = lower_bound(dp, input_list, input_list[i])
            dp[pos] = i
        LIS_arr.append(len(dp))
    return LIS_arr


if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            input_list = list(map(int, input().split()))
            input_len = len(input_list)
            dp_LIS = LIS(input_list)
            dp_LDS = LIS(input_list[::-1])
            wavio_len = 1
            for i in range(N):
                wavio_len = max(wavio_len, min(dp_LIS[i], dp_LDS[input_len - i - 1]) * 2 - 1)
            print(wavio_len)
        except:
            break
