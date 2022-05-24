"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 30/01/2022
"""

INF = int(1e9) + 7

factor = [0] * (2 * 10 ** 6 + 10)
factor[0] = 1
factor[1] = 1

for i in range(2, 2 * 10 ** 6 + 10):
    factor[i] = (i * factor[i - 1]) % INF


def get_exp(a, b, m):
    result = 1
    while b > 0:
        if b & 1 == 1:
            result = (result * a) % m
            b -= 1
        b >>= 1
        a = (a * a) % m
    return result


def count(n, k):
    if k == 1:
        return 1
    result_1 = factor[n + k - 1]
    # for i in range(n + 1, n + k):
    #     result_1 *= i
    #     result_1 %= INF
    result_2 = factor[k - 1] * factor[n]
    # for i in range(1, k):
    #     result_2 *= i
    #     result_2 %= INF
    convert_result_2 = get_exp(result_2, INF - 2, INF)
    return (result_1 * convert_result_2) % INF


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n, k = map(int, input().split())
        result = count(n, k)
        print("Case {}: {}".format(t + 1, result))
