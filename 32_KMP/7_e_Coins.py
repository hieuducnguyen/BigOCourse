"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 12/02/2022
"""
import sys

import math

INF = int(1e9)
sys.setrecursionlimit(10 ** 4 + 5)


def get_min_coin(a, b, dp, coin_list):
    if a < 0 or b < 0:
        return -1
    if dp[a][b] != -2:
        return dp[a][b]
    result = INF
    for x, y in coin_list:
        sub_min_coin = get_min_coin(a - x, b - y, dp, coin_list)
        if sub_min_coin >= 0:
            result = min(result, sub_min_coin + 1)
    if result == INF:
        dp[a][b] = -1
    else:
        dp[a][b] = result
    return dp[a][b]


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        input()
        M, S = map(int, input().split())
        if M == 0:
            print(0)
            continue
        value_list = []
        dup_set = set()
        for i in range(S):
            if i in dup_set:
                continue
            remain_val = int(math.sqrt(S ** 2 - i ** 2))
            if remain_val - math.sqrt(S ** 2 - i ** 2) == 0:
                dup_set.add(i)
                dup_set.add(remain_val)
                value_list.append((i, remain_val))
                value_list.append((remain_val, i))
        coin_list = []
        for m in range(M):
            x, y = map(int, input().split())
            coin_list.append((x, y))
        min_coin = INF
        dp = [[-1] * (S + 1) for _ in range(S + 1)]
        dp[0][0] = 0
        for i in range(S + 1):
            for j in range(S + 1):
                if dp[i][j] >= 0:
                    for x, y in coin_list:
                        if x + i <= S and y + j <= S:
                            dp[x + i][y + j] = min(dp[x + i][y + j], 1 + dp[i][j]) if dp[x + i][y + j] >= 0 else 1 + \
                                                                                                                 dp[i][
                                                                                                                     j]
        for a, b in value_list:
            coin = dp[a][b]
            if coin > 0:
                min_coin = min(min_coin, coin)
        if min_coin == INF:
            print("not possible")
        else:
            print(min_coin)
