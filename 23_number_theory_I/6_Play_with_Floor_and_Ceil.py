"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 30/01/2022
"""
import math


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        x, k = map(int, input().split())
        a = math.floor(x / k)
        b = math.ceil(x / k)
        # print(a, b)
        gcd, _x, _y = extended_gcd(a, b)
        # print("gcd {}, {}, {}".format(gcd, _x, _y))
        multi = x // gcd
        print(multi * _x, multi * _y)
