import random


def RSHash(key):
    hash_val = 0
    a = 63689
    b = 378551
    for i in range(len(key)):
        hash_val = hash_val * a + ord(key[i]) & 0x7FFFFFFF
        a = a * b & 0x7FFFFFFF
    return hash_val


def poly_hash(key):
    a = 33
    hash_val = 0
    for i in range(len(key)):
        hash_val = hash_val * a + ord(key[i]) & 0x7FFFFFFF
    return hash_val


if __name__ == '__main__':
    # hash_value = poly_hash("Algo")
    # print(hash_value)
    # exp_list = [1] * 10 ** 6
    for i in range(500000):
        print(str(random.randint(0, 1)), end="")
        # exp_list[i] = exp_list[i - 1] * 26
        # print(exp_list[-1])
