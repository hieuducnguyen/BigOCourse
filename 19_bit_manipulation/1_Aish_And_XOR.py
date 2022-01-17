"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 13/12/2021
"""


def XOR_num(num_list):
    result = 0
    num_zero = 0
    for num in num_list:
        if num == 0:
            num_zero += 1
        result ^= num
    return result, num_zero


if __name__ == '__main__':
    N = int(input())
    number_list = list(map(int, input().split()))
    xor_result = [0]
    tmp_result = 0
    num_zero = 0
    num_zero_list = [0]
    for num in number_list:
        tmp_result ^= num
        xor_result.append(tmp_result)
        if num == 0:
            num_zero += 1
        num_zero_list.append(num_zero)
    # print(xor_result)
    # print(num_zero_list)
    Q = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        print(xor_result[R] ^ xor_result[L - 1], num_zero_list[R] - num_zero_list[L - 1])
