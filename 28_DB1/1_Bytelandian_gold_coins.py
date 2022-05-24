"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 17/01/2022
"""


def max_coin(n, dp):
    if n < 10 ** 6 and dp[n] >= 0:
        return dp[n]
    if n < 10 ** 6:
        dp[n] = max(max_coin(n // 2, dp) + max_coin(n // 3, dp) + max_coin(n // 4, dp), n)
        return dp[n]
    else:
        return max(max_coin(n // 2, dp) + max_coin(n // 3, dp) + max_coin(n // 4, dp), n)


if __name__ == '__main__':
    dp = [-1] * (10 ** 6)
    dp[0] = 0
    dp[1] = 1
    for i in range(1, 10 ** 6):
        max_coin(i, dp)
    while True:
        try:
            N = int(input())
            # dp = [-1] * (N + 1)
            # dp[0] = 0
            # dp[1] = 1
            # for i in range(1, N + 1):
            print(max_coin(N, dp))
        except EOFError:
            break
