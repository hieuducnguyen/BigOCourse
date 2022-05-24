"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 13/02/2022
"""
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, W = map(int, input().split())
        test_list = []
        for n in range(N):
            C, P, time = map(int, input().split())
            test_list.append((P * C, time))
        dp = [[0] * (W + 1) for _ in range(len(test_list) + 1)]
        for i in range(1, len(test_list) + 1):
            for j in range(1, W + 1):
                test = test_list[i - 1]
                if test[1] <= j:
                    dp[i][j] = max(dp[i - 1][j], test[0] + dp[i - 1][j - test[1]])
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp[len(test_list)][W])
