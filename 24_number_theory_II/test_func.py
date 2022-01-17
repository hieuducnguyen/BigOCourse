"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 12/01/2022
"""


def checkPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def list_prime(N):
    result = [True] * (N + 1)
    result[0] = result[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if result[i]:
            for k in range(i * i, N + 1, i):
                result[k] = False
    primes = []
    for i in range(2, N):
        if result[i]:
            primes.append(i)
    return primes


def list_prime_segment(start, end):
    base_primes = list_prime(int(end ** 0.5) + 1)
    result = [True] * (end - start + 1)
    for prime in base_primes:
        base = start // prime
        base *= prime
        if base < start:
            base += prime
        for i in range(base, end + 1, prime):
            if base == prime:
                continue
            result[i - start] = False
    primes = []
    for i in range(start, end + 1):
        if result[i - start]:
            primes.append(i)
    print(primes)


if __name__ == '__main__':
    ##n = 7
    ##print(checkPrime(n))
    # n = 25
    # prime_list = list_prime(n)
    # for i in range(len(prime_list)):
    #    if prime_list[i]:
    #        print("number={} : is prime".format(i))
    #        print("number={} : is prime".format(i))
    list_prime_segment(10, 25)
