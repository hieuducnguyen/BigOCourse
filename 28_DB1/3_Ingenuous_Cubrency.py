"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 18/01/2022
"""


def method_name(N, dp):
    for i in range(1, 22):
        for j in range(coins[i], N + 1):
            dp[j] += dp[j - coins[i]]


if __name__ == '__main__':
    coins = [0] * 22
    for i in range(1, 22):
        coins[i] = i ** 3
    dp = [0] * (10000 + 1)
    dp[0] = 1
    method_name(10000, dp)
    while True:
        try:
            N = int(input())
            print(dp[N])
        except EOFError:
            break
