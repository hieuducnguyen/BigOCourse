"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


def compare_2_value(ladder):
    max_diff = 0
    for i in range(len(ladder)):
        base = 0 if i == 0 else ladder[i - 1]
        max_diff = max(max_diff, ladder[i] - base)
    return max_diff


def enough_height(k, ladder):
    for i in range(len(ladder)):
        base = 0 if i == 0 else ladder[i - 1]
        if k < (ladder[i] - base):
            return False
        if k == (ladder[i] - base):
            k -= 1
    return True


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        ladder = list(map(int, input().split()))
        max_k = compare_2_value(ladder)
        start, end = 0, max_k + 2
        result = -1
        while start < end:
            mid = (start + end) // 2
            if enough_height(mid, ladder):
                result = mid
                end = mid
            else:
                start = mid + 1
        print("Case {}: {}".format(i + 1, result))
