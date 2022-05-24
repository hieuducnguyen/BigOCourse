"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 22/01/2022
"""

factorial = [1, 1]
for i in range(2, 61):
    factorial.append(factorial[-1] * i)


def getCombination(K, N):
    if K > N:
        K, N = N, K
    K = K if K > 0 else 1
    return factorial[N] // (factorial[N - K] * factorial[K])


# print(factorial)


def diff(dp, pos_1, pos_2, text_1, text_2):
    if pos_1 == 0 and pos_2 == 0:
        return
    if text_1[pos_1] == text_2[pos_2]:
        diff(dp, pos_1 - 1, pos_2 - 1, text_1, text_2)
        print(" {}".format(text_1[pos_1]))
    elif dp[pos_1][pos_2 - 1] > dp[pos_1 - 1][pos_2]:
        diff(dp, pos_1, pos_2 - 1, text_1, text_2)
        print("+{}".format(text_2[pos_2]))
    else:
        diff(dp, pos_1 - 1, pos_2, text_1, text_2)
        print("-{}".format(text_1[pos_1]))


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
    diff(dp, len_text_1 - 1, len_text_2 - 1, text_1, text_2)
    # return len_text_1 + len_text_2 - dp[len_text_1][len_text_2], diff_case


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        text_1 = input()
        text_2 = input()
        LCS(text_1, text_2)
        # shorest_common, case = LCS(text_1, text_2)
        # print("Case {}: {} {}".format(t + 1, shorest_common, case))
