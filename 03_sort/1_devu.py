"""
Link: https://codeforces.com/problemset/problem/439/B
Time complexity: O(N * Log(N))
Space complexity: O(N)
"""


def count_time():
    n, x = map(int, input().split())
    chapter = list(map(int, input().split()))
    chapter.sort()
    result = 0
    for i in chapter:
        result += i * x
        if x > 1:
            x -= 1
    return result


if __name__ == '__main__':
    print(count_time())
