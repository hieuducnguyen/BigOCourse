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
            start = 0
            end = 10 ** 4 + 1
            func = CalculateFunc(p, q, r, s, t, u)
            val_end = func.calculate((end - 1) * 0.0001)
            val_start = func.calculate(start * 0.0001)
            if val_end > 0 or val_start < 0:
                print("No solution")
                continue
            while start < end:
                mid = (start + end) // 2
                val = func.calculate(mid * 0.0001)
                if val == 0:
                    print("{:.4f}".format(mid * 0.0001))
                    break
                if val > 0:
                    start = mid + 1
                else:
                    end = mid
            else:
                if abs(func.calculate(start * 0.0001)) > abs(func.calculate((start - 1) * 0.0001)):
                    print("{:.4f}".format((start - 1) * 0.0001))
                else:
                    print("{:.4f}".format(start * 0.0001))
        except EOFError as e:
            break
