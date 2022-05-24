"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 13/02/2022
"""
if __name__ == '__main__':
    N = int(input())
    for n in range(N):
        M = int(input())
        val_list = list(map(int, input().split()))
        sum_val_list = sum(val_list)
        max_weight = sum_val_list // 2
        dp = [[False] * (max_weight + 1) for _ in range(len(val_list) + 1)]
        ##for i in range(max_weight + 1):
        ##    dp[0][i] = True
        for i in range(len(val_list) + 1):
            dp[i][0] = True
        for i in range(1, len(val_list) + 1):
            for j in range(1, max_weight + 1):
                val = j - val_list[i - 1]
                if val >= 0:
                    dp[i][j] = dp[i - 1][j - val_list[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        one_w = 0
        for i in range(max_weight, max_weight - max(val_list) - 1, -1):
            if dp[len(val_list)][i]:
                one_w = i
                break
        print(abs(one_w - (sum_val_list - one_w)))
