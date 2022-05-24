"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 15/01/2022
"""

a = 29
INF = int(1e17 + 7)


def hash_string(tmp_strg):
    val_hash = 0
    prefix_hash = []
    for val in tmp_strg:
        val_hash = (val_hash * a + ord(val) - ord("a") + 1) % INF
        prefix_hash.append(val_hash)
    return prefix_hash


def get_hash_val(start, end, prefix_hash, power):
    if start == 0:
        return prefix_hash[end]
    return (prefix_hash[end] - prefix_hash[start - 1] * power[end - start + 1] % INF + INF) % INF


# if __name__ == '__main__':
#     power = [1] * 1501
#     for i in range(1, 1500 + 1):
#         power[i] = (power[i - 1] * a) % INF
#     prefix_hash = hash_string("dcba")
#     hash_val = get_hash_val(1, 2, prefix_hash, power)
#     print(hash_val)
if __name__ == '__main__':
    strg = input()
    good_char_list = list(map(int, list(input())))
    K = int(input())
    good_char = set()
    for i in range(26):
        if good_char_list[i] == 1:
            good_char.add(i)
    power = [1] * 1501
    for i in range(1, 1500 + 1):
        power[i] = (power[i - 1] * a) % INF
    prefix_hash = hash_string(strg)
    # print("finish prefix hash")
    good_string_set = set()
    for i in range(len(strg)):
        bad_char = 0
        for j in range(i, len(strg)):
            if not good_char.__contains__(ord(strg[j]) - ord("a")):
                bad_char += 1
            if bad_char > K:
                break
            hash_val = get_hash_val(i, j, prefix_hash, power)
            good_string_set.add(hash_val)
            # if j % 1000 == 0:
            #     print("j val {}".format(j))
    print(len(good_string_set))
