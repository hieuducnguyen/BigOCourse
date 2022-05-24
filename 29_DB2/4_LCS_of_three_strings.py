"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 22/01/2022
"""


def count_LCS(word_1, word_2, word_3):
    len_word_1 = len(word_1)
    len_word_2 = len(word_2)
    len_word_3 = len(word_3)
    dp = [[[0] * (len_word_3 + 1) for _ in range(len_word_2 + 1)] for _ in range(len_word_1 + 1)]

    for i in range(1, len_word_1 + 1):
        for j in range(1, len_word_2 + 1):
            for k in range(1, len_word_3 + 1):
                if word_1[i - 1] == word_2[j - 1] == word_3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i][j - 1][k], dp[i - 1][j][k], dp[i][j][k - 1])
    return dp[len_word_1][len_word_2][len_word_3]


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n, m, k = map(int, input().split())
        x, y, z = input().split()
        result = count_LCS(x, y, z)
        print(result)
