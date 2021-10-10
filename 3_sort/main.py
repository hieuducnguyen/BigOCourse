"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def foo(n):
    if n == 0:
        return 1.0
    else:
        sum_ = 0
        for i in range(n):
            sum_ += foo(i)
        return sum_


if __name__ == '__main__':
    print(foo(3))
