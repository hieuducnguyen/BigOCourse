"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def max_book():
    N, T = map(int, input().split())
    time_book = list(map(int, input().split()))
    start_window, end_window = 0, 0
    num_book, time, max_book = 0, 0, 0
    while end_window < len(time_book):
        time += time_book[end_window]
        num_book += 1
        while time > T:
            time -= time_book[start_window]
            num_book -= 1
            start_window += 1
        max_book = max(max_book, num_book)
        end_window += 1
    return max_book


if __name__ == '__main__':
    print(max_book())
