"""
Link: https://codeforces.com/problemset/problem/448/B
Time complexity: O(n)
Space complexity: O(n)
"""
import collections


def is_subsequence(s, t):
    start_t = 0
    new_s = ''
    for i in s:
        if i == t[start_t]:
            new_s += i
            start_t += 1
            if start_t == len(t):
                break
    return new_s == t


def check_suffix():
    s = input()
    t = input()
    counter_s = collections.Counter(s)
    counter_t = collections.Counter(t)
    for k, v in counter_t.items():
        if k not in counter_s or counter_s[k] < counter_t[k]:
            print("need tree")
            return
    if len(s) == len(t):
        print("array")
    elif is_subsequence(s, t):
        print("automaton")
    else:
        print("both")


if __name__ == '__main__':
    check_suffix()

    
