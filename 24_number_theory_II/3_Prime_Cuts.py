"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 13/01/2022
"""


def get_primes(N):
    mark = [True] * (N + 1)
    mark[0] = False
    mark[1] = True
    for i in range(2, int(N ** 0.5) + 1):
        if mark[i]:
            for k in range(i * i, N + 1, i):
                mark[k] = False
    primes = []
    for i in range(1, N + 1):
        if mark[i]:
            primes.append(i)
    return primes


if __name__ == '__main__':
    while True:
        try:
            N, C = map(int, input().split())
            primes = get_primes(N)
            if len(primes) & 1 > 0:
                if 2 * C - 1 < len(primes):
                    pos = (len(primes) - (2 * C - 1)) // 2
                    cutted_primes = primes[pos: len(primes) - pos]
                else:
                    cutted_primes = primes
            else:
                if 2 * C < len(primes):
                    pos = (len(primes) - (2 * C)) // 2
                    cutted_primes = primes[pos: len(primes) - pos]
                else:
                    cutted_primes = primes
            print("{} {}: ".format(N, C), end="")
            print(*cutted_primes, sep=" ")
            print()
        except EOFError:
            break
