"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 12/02/2022
"""
BASE = 29
INF = int(1e17 + 7)
POWER = [1] * (10 ** 5 + 5)
for i in range(1, 10 ** 5 + 5):
    POWER[i] = (POWER[i - 1] * BASE) % INF


def get_hash(text):
    hash_val = [0] * len(text)
    hash_val[0] = ord(text[0]) - ord("a") + 1
    for i in range(1, len(text)):
        hash_val[i] = (hash_val[i - 1] * BASE + ord(text[i]) - ord("a") + 1) % INF
    return hash_val


def get_hash_range(hash_val, start, end):
    if start == 0:
        return hash_val[end]
    return (hash_val[end] - hash_val[start - 1] * POWER[end - start + 1] + INF) % INF


if __name__ == '__main__':
    while True:
        input_text = input()
        hash_val = get_hash(input_text)
        if input_text == "*":
            break
        for i in range(1, len(input_text) - 1):
            if len(input_text) % i != 0:
                continue
            sub_hash = get_hash_range(hash_val, 0, i - 1)
            for j in range(i, len(input_text) - i + 1, i):
                hash_range = get_hash_range(hash_val, j, j + i - 1)
                if hash_range != sub_hash:
                    break
            else:
                print(len(input_text) // i)
                break
        else:
            print(1)
