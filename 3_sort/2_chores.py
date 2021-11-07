"""
Link: https://codeforces.com/problemset/problem/169/A
Author: Nguyen Duc Hieu
"""

"""
Time complexity: O(N * log(N))
Space complexity: O(N)
"""


def method_1():
    n, a, b = map(int, input().split())
    jobs = list(map(int, input().split()))
    jobs.sort()
    print(jobs[-a] - jobs[b - 1])


def quick_selection(vals, index, start, end):
    pivot = vals[end]
    j = -1
    for i in range(start, end + 1):
        if vals[i] < pivot:
            j += 1
            vals[i], vals[j] = vals[j], vals[i]
    vals[end], vals[j + 1] = vals[j + 1], vals[end]
    if 


def method_2():
    n, a, b = map(int, input().split())
    jobs = list(map(int, input().split()))
    val_vasya = quick_selection(jobs, b - 1, 0, len(jobs) - 1)
    val_petya = quick_selection(jobs, len(jobs) - a, 0, len(jobs) - 1)
    print(val_petya - val_vasya)


if __name__ == '__main__':
    method_2()
