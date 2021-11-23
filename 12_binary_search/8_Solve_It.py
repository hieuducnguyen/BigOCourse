"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1282
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

import math


class CalculateFunc:
    def __init__(self, p, q, r, s, t, u):
        self.u = u
        self.t = t
        self.s = s
        self.r = r
        self.q = q
        self.p = p

    def calculate(self, x):
        return self.p * math.e ** (-x) + self.q * math.sin(x) + self.r * math.cos(x) + self.s * math.tan(
            x) + self.t * x ** 2 + self.u


if __name__ == '__main__':
    while True:
        try:
            p, q, r, s, t, u = map(int, input().split())
            func = CalculateFunc(p, q, r, s, t, u)
            if func.calculate(0) < 0 or func.calculate(1) > 0:
                print("No solution")
                continue
            start, end, mid = 0, 1, 0
            while end - start > 10 ** (-5):
                mid = start + (end - start) / 2
                if func.calculate(mid) == 0:
                    break
                elif 0 < func.calculate(mid):
                    start = mid
                else:
                    end = mid
            mid = start + (end - start) / 2
            print(format(mid, ".4f"))
            # print("{:.4f}".format(mid))
        except EOFError:
            break
