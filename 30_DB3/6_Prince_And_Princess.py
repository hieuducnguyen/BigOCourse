"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 27/01/2022
"""


def lower_bound(dp, arr, key):
    start = 0
    end = result = len(dp)
    while start < end:
        mid = start + (end - start) // 2
        if arr[dp[mid]] >= key:
            end = mid
            result = mid
        else:
            start = mid + 1
    return result


def LIS(arr):
    if not arr:
        return 0
    dp = [0]
    for i in range(1, len(arr)):
        if arr[i] < arr[dp[0]]:
            dp[0] = i
        elif arr[i] > arr[dp[-1]]:
            dp.append(i)
        else:
            pos = lower_bound(dp, arr, arr[i])
            dp[pos] = i
    return len(dp)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n, p, q = map(int, input().split())
        p_list = list(map(int, input().split()))
        arr_1 = [-1] * 62501
        for i in range(len(p_list)):
            arr_1[p_list[i]] = i
        q_list = list(map(int, input().split()))
        arr = []
        for val in q_list:
            if arr_1[val] >= 0:
                arr.append(arr_1[val])
        LIS_len = LIS(arr)
        print("Case {}: {}".format(t + 1, LIS_len))
