"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 22/01/2022
"""


def LCS(friend, agne):
    len_agne = len(agne)
    len_friend = len(friend)
    dp = [[0] * (len_friend + 1) for _ in range(len_agne + 1)]
    for i in range(1, len_agne + 1):
        for j in range(1, len_friend + 1):
            if agne[i - 1] == friend[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len_agne][len_friend] - 1


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        agne = list(map(int, input().split()))
        friend_list = []
        while True:
            input_text = input()
            if input_text == "0":
                break
            friend_list.append(list(map(int, input_text.split())))
        max_common = 0
        for friend in friend_list:
            max_common = max(max_common, LCS(friend, agne))
        print(max_common)
