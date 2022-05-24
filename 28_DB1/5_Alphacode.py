"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 18/01/2022
"""
if __name__ == '__main__':
    while True:
        N = input()
        if N == "0":
            break
        input_list = list(map(int, list(N)))
        dp = [0] * (len(input_list) + 1)
        dp[0] = 1
        for i in range(1, len(input_list) + 1):
            if input_list[i - 1] >= 1:
                dp[i] = dp[i - 1]
            if i - 2 >= 0 and input_list[i - 2] != 0 and (input_list[i - 2] * 10 + input_list[i - 1] <= 26):
                dp[i] += dp[i - 2]
        print(dp[len(input_list)])
