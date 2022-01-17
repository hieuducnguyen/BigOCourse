"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 15/01/2022
"""
from collections import defaultdict


def sum_digits(N):
    total = 0
    while N:
        total += N % 10
        N //= 10
    return total


def r3gz3n(N):
    return N ^ sum_digits(N)


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    list_val = []
    frequent = defaultdict(list)
    max_fre = 0
    max_fre_hash_set = set()
    uniq = True
    colision = 0
    for num in nums:
        hash_val = r3gz3n(num)
        if len(frequent[hash_val]) > 0:
            colision += 1
        frequent[hash_val].append(num)
        if len(frequent[hash_val]) > max_fre:
            max_fre = len(frequent[hash_val])
            max_fre_hash_set = {hash_val}
        elif len(frequent[hash_val]) == max_fre:
            max_fre_hash_set.add(hash_val)
        if len(frequent[hash_val]) > 1:
            uniq = False
    if uniq:
        print(max(frequent), colision)
    else:
        print(min(max_fre_hash_set), colision)
