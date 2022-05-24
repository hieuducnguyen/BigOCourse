"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 08/02/2022
"""

BASE = 29
INF = 10 * 9 + 7
BASE_FACTOR = [1] * 10 ** 5
for i in range(1, 10 ** 5):
    BASE_FACTOR[i] = BASE * BASE_FACTOR[i - 1] % INF


def get_hash_val(text, start, end, hash_val):
    if start == 0:
        return hash_val[end]
    return (hash_val[end] - hash_val[start - 1]) % INF


def gen_hash_val(text):
    hash_val = [0] * len(text)
    for i in range(len(text)):
        hash_val[i] = ((ord(text[i]) - ord("a") + 1) * BASE + hash_val[i - 1]) % INF
    return hash_val


def check_valid(bin_text, text_first_pattern, start, hash_val, hash_of_fist_pattern, len_text):
    hash_of_second_pattern = -1
    first_iterator = 1
    while start < len_text:
        if bin_text[first_iterator] == 0:
            if hash_of_fist_pattern != get_hash_val(text, start, start + len(text_first_pattern) - 1, hash_val):
                return False
            start += len(text_first_pattern)
        else:
            if hash_of_second_pattern == -1:
                hash_of_second_pattern = get_hash_val(text, start, start + len_second_pattern - 1, hash_val)
                if hash_of_second_pattern == hash_of_fist_pattern:
                    return False
            else:
                if hash_of_second_pattern != get_hash_val(text, start, start + len_second_pattern - 1, hash_val):
                    return False
            start += len_second_pattern
        first_iterator += 1
    return True


if __name__ == '__main__':
    bin_text = list(map(int, input()))
    first_pattern = str(bin_text[0])
    text = input()
    hash_val = gen_hash_val(text)
    num_1 = sum(bin_text)
    num_0 = len(bin_text) - num_1
    if first_pattern == "0":
        num_first_pattern = num_0
        num_second_pattern = num_1
    else:
        num_first_pattern = num_1
        num_second_pattern = num_0
    num_right = 0
    for i in range(1, len(text)):
        text_first_pattern = text[:i]
        if (len(text) - len(text_first_pattern) * num_first_pattern) % num_second_pattern != 0 or (
                len(text) - len(text_first_pattern) * num_first_pattern) // num_second_pattern < 1:
            continue
        len_second_pattern = (len(text) - len(text_first_pattern) * num_first_pattern) // num_second_pattern
        hash_of_fist_pattern = get_hash_val(text, 0, i - 1, hash_val)
        start = len(text_first_pattern)
        if check_valid(bin_text, text_first_pattern, start, hash_val, hash_of_fist_pattern, len(text)):
            num_right += 1
    print(num_right)
