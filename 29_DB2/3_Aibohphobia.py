"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 22/01/2022
"""


def LCS(text_1, text_2):
    len_text_1 = len(text_1)
    len_text_2 = len(text_2)
    dp = [[0] * (len_text_2 + 1) for _ in range(len_text_1 + 1)]
    for i in range(1, len_text_1 + 1):
        for j in range(1, len_text_2 + 1):
            if text_1[i - 1] == text_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len_text_1][len_text_2]


if __name__ == '__main__':
    s = input()
    len_LCS = LCS(s, s[::-1])
    print(len(s) - len_LCS)
