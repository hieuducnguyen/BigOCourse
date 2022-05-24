"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 12/02/2022
"""
BASE = 33
INF = int(1e9 + 7)
POWER = [1] * (10 ** 5 + 5)
for i in range(1, 10 ** 5 + 5):
    POWER[i] = (POWER[i - 1] * BASE) % INF


def get_hash_range(hash_val, start, end):
    if start == 0:
        return hash_val[end]
    return (hash_val[end] - hash_val[start - 1] * POWER[end - start + 1]) % INF


def get_hash_val(text):
    hash_val = [0] * len(text)
    hash_val[0] = ord(text[0]) - ord("a") + 1
    for i in range(1, len(text)):
        hash_val[i] = (hash_val[i - 1] * BASE + ord(text[i]) - ord("a") + 1) % INF
    return hash_val


def pass_sub_str(hash_sub_string, full_text_hash_arr, num_require, len_sub_txt):
    num_equal = 0
    for i in range(len(full_text_hash_arr) - len_sub_txt + 1):
        if get_hash_range(full_text_hash_arr, i, i + len_sub_txt - 1) == hash_sub_string:
            num_equal += 1
    return num_equal >= num_require


if __name__ == '__main__':
    full_text = input()
    sub_text = input()
    num_require = int(input())
    full_text_hash_arr = get_hash_val(full_text)
    sub_text_hash_arr = get_hash_val(sub_text)
    start = 0
    end = len(sub_text)
    result = end
    while start < end:
        mid = start + (end - start) // 2
        if pass_sub_str(sub_text_hash_arr[mid], full_text_hash_arr, num_require, mid + 1):
            start = mid + 1
            result = mid
        else:
            end = mid
    if result == len(sub_text):
        print("IMPOSSIBLE")
    else:
        print(sub_text[:result + 1])
