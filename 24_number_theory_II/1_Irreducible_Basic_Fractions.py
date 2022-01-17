"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 12/01/2022
"""


def count(N):
    result = N
    for i in range(2, int(N ** 0.5) + 1):
        if N % i != 0:
            continue
        while N % i == 0:
            N //= i
        result = result * (i - 1) // i
    if N > 1:
        result = result * (N - 1) // N
    return result


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        print(count(N))
