"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 13/01/2022
"""


def LPD(N):
    largest_prime_divisor = -1
    val = N
    num_prime = 0
    for i in range(2, int(N ** 0.5) + 1):
        if val % i == 0:
            num_prime += 1
            largest_prime_divisor = max(largest_prime_divisor, i)
            while val % i == 0:
                val //= i
    if val > 1 and val != N:
        num_prime += 1
        largest_prime_divisor = max(largest_prime_divisor, val)
    return largest_prime_divisor if num_prime > 1 else -1


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        print(LPD(abs(N)))
