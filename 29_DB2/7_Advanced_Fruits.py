"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 22/01/2022
"""


def LCS(name_1, name_2):
    len_name_1 = len(name_1)
    len_name_2 = len(name_2)
    dp = [[0] * (len_name_2 + 1) for _ in range(len_name_1 + 1)]
    for i in range(1, len_name_1 + 1):
        for j in range(1, len_name_2 + 1):
            if name_1[i - 1] == name_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i = len_name_1
    j = len_name_2
    result = []
    while i > 0 and j > 0:
        if name_1[i - 1] == name_2[j - 1]:
            result.append(name_1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            result.append(name_1[i - 1])
            i -= 1
        else:
            result.append(name_2[j - 1])
            j -= 1
    if i > 0:
        result.extend(list(name_1[:i])[::-1])
    if j > 0:
        result.extend(list(name_2[:j])[::-1])
    result.reverse()
    return result


if __name__ == '__main__':
    while True:
        try:
            name_1, name_2 = input().split()
            result = LCS(name_1, name_2)
            print(*result, sep="")
        except EOFError:
            break
