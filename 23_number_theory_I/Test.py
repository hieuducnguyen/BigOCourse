def modularExponentiation(a, b, m):
    result = 1
    a %= m
    for i in range(b):
        result *= a
        result %= m
    return result


def modularExponentiation1(a, b, m):
    a %= m
    result = 1
    while b != 0:
        if b & 1 > 0:
            result = result * a
            result %= m
            b -= 1
        a = (a * a) % m
        b >>= 1
    return result


if __name__ == '__main__':
    a = 50
    b = 100
    m = 13
    # a = 5
    # b = 5
    # m = 8
    val = modularExponentiation1(a, b, m)
    print(val)
