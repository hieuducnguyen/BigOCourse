def modularExponentiation(a, b, m):
    result = 1
    a %= m
    for i in range(b):
        result *= a
        result %= m
    return result


def modularExponentiation1(a, b, m):
    result = 1
    while b > 0:
        if b & 1 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b >>= 1
    return result


INF = int(1e9) + 7


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


if __name__ == '__main__':
    gcd, x, y = extended_gcd(22, 17)
    print(gcd)
    print(x)
    print(y)
