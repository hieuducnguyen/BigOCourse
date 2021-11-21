"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""
import bisect


def sort_student():
    N = map(int, input())
    rate_list = list(map(int, input().split()))
    sorted_rate = sorted(rate_list)
    for i in rate_list:
        print(len(rate_list) - bisect.bisect_right(sorted_rate, i) + 1, end=" ")


if __name__ == '__main__':
    sort_student()
