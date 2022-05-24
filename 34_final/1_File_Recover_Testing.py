"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 21/02/2022
"""
INF = int(1e9 + 7)
BASE = 33

POWER = [0] * (10 ** 9 + 5)
POWER[0] = 1
for i in range(1, 10 ** 9 + 5):
    print(i)
    POWER[i] = (POWER[i - 1] * BASE) % INF


def get_hash_range(start, end, arr_hash):
    if start == 0:
        return arr_hash[end]
    return (arr_hash[end] - arr_hash[start - 1] * POWER[end - start + 1]) % INF


def get_hash(text):
    arr_hash = [0] * len(text)
    arr_hash[0] = ord(text[0]) - ord('a') + 1
    for i in range(1, len(text)):
        arr_hash[i] = (arr_hash[i - 1] * BASE + ord(text[0]) - ord('a') + 1) % INF
    return arr_hash


if __name__ == '__main__':
    while True:
        print(len(POWER))
        len_text_str, pattern = input().split()
        if len_text_str == "-1":
            break
        len_text = int(len_text_str)
        len_pattern = len(pattern)
        num_pattern = len_text // len_pattern
        text = pattern * num_pattern + pattern[0:len_text % len_pattern]
        arr_hash_text = get_hash(text)
        arr_hash_pattern = get_hash(pattern)
        num_equal = 0
        for i in range(len(text) - len(pattern) + 1):
            if get_hash_range(i + len(pattern) - 1, i, arr_hash_text) == arr_hash_pattern[-1]:
                num_equal += 1
        print(num_equal)
