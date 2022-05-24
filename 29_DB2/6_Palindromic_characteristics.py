"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 23/01/2022
"""
from collections import defaultdict

BASE = 33
INF = int(1e9 + 7)

power = [1] * 5001
for i in range(1, 5001):
    power[i] = power[i - 1] * BASE % INF


def get_prefix_hash(char_list):
    prefix_list = []
    hash_val = 0
    for char_item in char_list:
        hash_val = (hash_val * BASE + ord(char_item) - ord("a") + 1) % INF
        prefix_list.append(hash_val)
    return prefix_list


def get_hash_range(start, end, prefix_hash):
    if start == 0:
        return prefix_hash[end]
    return (prefix_hash[end] - prefix_hash[start - 1] * power[end - start + 1]) % INF


def get_palindromic(x, y, len_text):
    len_sub = y - x + 1
    palindromic_list = []
    if y + 1 + len_sub - 1 <= len_text - 1:
        palindromic_list.append((y + 1, y + 1 + len_sub - 1))
    if y + 2 + len_sub - 1 <= len_text - 1:
        palindromic_list.append((y + 2, y + 2 + len_sub - 1))
    if x - 1 - (len_sub - 1) >= 0:
        palindromic_list.append((x - 1 - (len_sub - 1), x - 1))
    if x - 2 - (len_sub - 1) >= 0:
        palindromic_list.append((x - 2 - (len_sub - 1), x - 2))
    return palindromic_list


if __name__ == '__main__':
    text = input()
    len_text = len(text)
    char_list = list(text)
    reverse_char_list = char_list[::-1]
    prefix_hash = get_prefix_hash(char_list)
    reverse_prefix_hash = get_prefix_hash(reverse_char_list)
    # print(prefix_hash)
    # print(reverse_prefix_hash)
    map_palindromic = defaultdict(set)
    result = []
    for i in range(len_text):
        for j in range(i, len_text):
            hash_range = get_hash_range(i, j, prefix_hash)
            reverse_hash_range = get_hash_range(len_text - 1 - j, len_text - 1 - i, reverse_prefix_hash)
            if hash_range == reverse_hash_range:
                map_palindromic[1].add((i, j))
                # print(text[i:j + 1])
    result.append(len(map_palindromic[1]))
    print(result)
    for i in range(2, len_text + 1):
        palindromic_set = map_palindromic[i - 1]
        if len(palindromic_set) != 0:
            for x, y in palindromic_set:
                # x, y = get_xy(val)
                palindromic_list = get_palindromic(x, y, len_text)
                for u, v in palindromic_list:
                    if get_hash_range(x, y, prefix_hash) == get_hash_range(u, v, prefix_hash):
                        if v > x:
                            map_palindromic[i].add((x, v))
                        else:
                            map_palindromic[i].add((u, y))
        print(map_palindromic[i])
        result.append(len(map_palindromic[i]))
        map_palindromic[i - 1] = set()
        print(result)
    print(*result, sep=" ")
