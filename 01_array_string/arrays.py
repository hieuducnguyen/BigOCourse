"""
Link: https://codeforces.com/contest/572/problem/A
Time complexity: O(n)
Space complexity: O(n)
"""


def check_arrays():
    input()
    n_a, n_b = map(int, input().split())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))
    return array_a[n_a - 1] < array_b[-n_b]


if __name__ == '__main__':
    if check_arrays():
        print("YES")
    else:
        print("NO")
