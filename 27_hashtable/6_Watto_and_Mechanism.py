"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 20/01/2022
"""
from collections import defaultdict

BASE = 5
INF = int(1e10 + 7)


def get_prefix(strg, power):
    prefix_hash = []
    hash_val = 0
    for i in range(len(strg)):
        hash_val = (hash_val * BASE + ord(strg[i]) - ord("a") + 1) % INF
        prefix_hash.append(hash_val)
    return prefix_hash


def get_hash(hash_list, start, end, power):
    if start == 0:
        return hash_list[end]
    return (hash_list[end] - hash_list[start - 1] * power[end - start + 1]) % INF


def compare_hash(hash_query, hash_base, power):
    if len(hash_query) != len(hash_base):
        return False
    start = 0
    for i in range(len(hash_query)):
        if get_hash(hash_query, start, i, power) != get_hash(hash_base, start, i, power):
            start = i + 1
            return get_hash(hash_query, start, len(hash_query) - 1, power) == get_hash(hash_base, start,
                                                                                       len(hash_query) - 1, power)
    return False


def method_name():
    N, M = map(int, input().split())
    power = [1] * (6 * 10 ** 5 + 1)
    for i in range(1, 6 * 10 ** 5 + 1):
        power[i] = power[i - 1] * BASE % INF
    hash_val_map = defaultdict(list)
    for i in range(N):
        s = input()
        prefix_hash = get_prefix(s, power)
        hash_val_map[len(s)].append(prefix_hash)
    hash_query_list = []
    for i in range(M):
        prefix_query_hash = get_prefix(input(), power)
        hash_query_list.append(prefix_query_hash)
    for i in range(M):
        hash_query = hash_query_list[i]
        compare_hash_list = hash_val_map[len(hash_query)]
        for compare_hash_val in compare_hash_list:
            if compare_hash(hash_query, compare_hash_val, power):
                print("YES")
                break
        else:
            print("NO")


def convert(strg):
    result = 0
    for val in strg:
        if val == "a":
            result = result << 2
        elif val == "b":
            result = result << 2 | 1
        else:
            result = result << 2 | 2
    return result


def count1(result):
    count = 0
    while result != 0:
        result &= (result - 1)
        count += 1
        if count > 2:
            return count
    return count


def compare2strg(val, val1):
    result = val ^ val1
    if result == 0:
        return False
    num_1 = count1(result)
    if num_1 == 1:
        return True
    if num_1 > 2:
        return False
    while result > 0:
        if result == 3:
            return True
        result >>= 2
    else:
        return False


if __name__ == '__main__':
    # val = convert("ab")
    # val1 = convert("ba")
    # result = compare2strg(val, val1)
    # print(result)
    N, M = map(int, input().split())
    hash_val_map = defaultdict(list)
    for n in range(N):
        s = input()
        hash_val = convert(s)
        hash_val_map[len(s)].append(hash_val)
    query_hash_list = []
    for m in range(M):
        query = input()
        hash_val = convert(query)
        query_hash = hash_val_map[len(query)]
        for query in query_hash:
            if compare2strg(hash_val, query):
                print("YES")
                break
        else:
            print("NO")
