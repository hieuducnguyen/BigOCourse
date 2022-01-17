"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 15/01/2022
"""

a = 29
INF = int(10 ** 9 + 7)


def poly_hash(key):
    prefix_hash_list = []
    hash_val = 0
    for i in range(len(key)):
        hash_val = (hash_val * a + (ord(key[i]) - ord("a"))) % INF
        prefix_hash_list.append(hash_val)
    return prefix_hash_list


def hash_range(start, end, prefix_hash, exp_list):
    return (prefix_hash[end] - prefix_hash[start] * exp_list[end - start]) % INF


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        strg = input()
        result = 0
        len_strg = len(strg)
        prefix_hash = poly_hash(strg)
        # print("prefix " + str(len(prefix_hash)) + "num :" + str(prefix_hash[-1]))
        start, end = 0, len(strg) - 1
        exp_list = [1] * len_strg
        # print("relocate")
        for i in range(1, len_strg):
            exp_list[i] = (exp_list[i - 1] * a) % INF
        # print("exp")
        while start < len(strg) - 1:
            val_range = hash_range(end - 1, len(strg) - 1, prefix_hash, exp_list)
            if prefix_hash[start] == val_range:
                result += 1
            # if start % 1000 == 0:
            #     print(start)
            start += 1
            end -= 1
        print("Case {}: {}".format(t + 1, result))
