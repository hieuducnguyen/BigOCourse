"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 14/01/2022
"""
import math

phi_list = [0] * 50001


def phi(num):
    src_num = num
    if phi_list[src_num] > 0:
        return phi_list[src_num]
    result = num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            while num % i == 0:
                num //= i
            result = result / i * (i - 1)
    if num > 1:
        result = result / num * (num - 1)
    phi_list[src_num] = result
    return result


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        result = 1
        for i in range(2, N + 1):
            result += int((phi(i) * 2))
        print(result)
