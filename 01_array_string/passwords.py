"""
Link: https://codeforces.com/contest/721/problem/B
Time complexity: O(n)
Space complexity: O(n)
"""


def time(num_try, stop_time):
    return num_try + (num_try - 1) // stop_time * 5


def check_pass():
    N, K = map(int, input().split())
    input_list = []
    for i in range(N):
        input_list.append(input())
    password = input()
    num_wrong_pass = len(list(filter(lambda x: len(x) < len(password), input_list)))
    equal_len_pass = len(list(filter(lambda x: len(x) == len(password), input_list)))
    print(time(num_wrong_pass + 1, K), time(num_wrong_pass + equal_len_pass, K))


if __name__ == '__main__':
    check_pass()
