"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 12/02/2022
"""

BASE = 33
POWER_ARR = [1] * 100005
INF = int(10 ** 9 + 7)
for i in range(1, 100005):
    POWER_ARR[i] = (POWER_ARR[i - 1] * BASE) % INF


def get_hash(input_text):
    hash_arr = [0] * len(input_text)
    hash_arr[0] = ord(input_text[0]) - ord("a") + 1
    for i in range(1, len(input_text)):
        hash_arr[i] = (BASE * hash_arr[i - 1] + (ord(input_text[i]) - ord("a") + 1)) % INF
    return hash_arr


def get_hash_range(hash_arr, start, end):
    if start == 0:
        return hash_arr[end]
    return (hash_arr[end] - hash_arr[start - 1] * POWER_ARR[end - start + 1]) % INF


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        input_text = input().replace(" ", "")
        sub_str = input()
        hash_arr = get_hash(input_text)
        sub_str_hash_arr = get_hash(sub_str)
        hash_sub_str = sub_str_hash_arr[len(sub_str) - 1]
        result = 0
        for i in range(len(input_text) - len(sub_str) + 1):
            if hash_sub_str == get_hash_range(hash_arr, i, i + len(sub_str) - 1):
                result += 1
        print("Case {}: {}".format(t + 1, result))
