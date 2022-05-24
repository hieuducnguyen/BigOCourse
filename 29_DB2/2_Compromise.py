"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 22/01/2022
"""


def LCS(words_1, words_2):
    len_words_1 = len(words_1)
    len_words_2 = len(words_2)
    dp = [[0] * (len_words_2 + 1) for _ in range(len_words_1 + 1)]
    for i in range(1, len_words_1 + 1):
        for j in range(1, len_words_2 + 1):
            if words_1[i - 1] == words_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i = len_words_1
    j = len_words_2
    LCS_len = dp[i][j]
    result = [""] * LCS_len
    while i >= 0 and j >= 0:
        if words_1[i - 1] == words_2[j - 1]:
            result[LCS_len - 1] = words_1[i - 1]
            i -= 1
            j -= 1
            LCS_len -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return result


if __name__ == '__main__':
    while True:
        try:
            text_1 = ""
            while True:
                tmp_txt = input()
                if tmp_txt == "#":
                    break
                text_1 += " " + tmp_txt
            text_2 = ""
            while True:
                tmp_txt = input()
                if tmp_txt == "#":
                    break
                text_2 += " " + tmp_txt
            # print(text_1)
            # print(text_2)
            words_1 = list(text_1.split())
            words_2 = list(text_2.split())
            result = LCS(words_1, words_2)
            print(*result, sep=" ")
        except EOFError as e:
            break
