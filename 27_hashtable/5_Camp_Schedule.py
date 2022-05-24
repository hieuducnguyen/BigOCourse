"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 17/01/2022
"""
import copy

INF = int(1e9 + 7)
BASE = 3


def get_prefix(t):
    prefix_patt = []
    hash_val = 0
    for i in range(len(t)):
        hash_val = (hash_val * BASE + ord(t[i]) - ord("0") + 1) % INF
        prefix_patt.append(hash_val)
    return prefix_patt


if __name__ == '__main__':
    s = input()
    t = input()
    input_s = list(map(int, list(s)))
    input_t = list(map(int, list(t)))
    power_list = [1]
    for i in range(1, 5 * int(1e5)):
        val = power_list[i - 1] * BASE % INF
        power_list.append(val)
    len_patt = len(input_t)
    longest_prefix_surfix = 0
    prefix_patt = get_prefix(t)
    for i in range(len_patt - 1):
        surfix = (prefix_patt[len_patt - 1] - prefix_patt[len_patt - 1 - i - 1] * power_list[i + 1] + INF) % INF
        if prefix_patt[i] == surfix:
            longest_prefix_surfix = max(longest_prefix_surfix, i + 1)
        # print(i)
    num_1 = sum(input_s)
    num_0 = len(input_s) - num_1
    num_1_t = sum(input_t)
    num_0_t = len(input_t) - num_1_t
    result = []
    if num_1 >= num_1_t and num_0 >= num_0_t:
        result.extend(input_t)
        num_0 -= num_0_t
        num_1 -= num_1_t

    need_1 = sum(input_t) - sum(input_t[0:longest_prefix_surfix])
    need_0 = len_patt - longest_prefix_surfix - need_1
    remain = copy.deepcopy(input_t[longest_prefix_surfix:])
    del input_t
    del input_s
    del power_list
    while num_0 >= need_0 and num_1 >= need_1:
        result.extend(remain)
        num_0 -= need_0
        num_1 -= need_1
    result.extend([0] * num_0)
    result.extend([1] * num_1)
    print(*result, sep="")
