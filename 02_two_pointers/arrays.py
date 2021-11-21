"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def minimum_segment():
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    frequency_map = {}
    start_window, end_window, counter, min_len, start_min, end_min = 0, 0, 0, len(array) + 1, -1, -1
    while end_window < len(array):
        frequency_map[array[end_window]] = frequency_map.get(array[end_window], 0) + 1
        if frequency_map[array[end_window]] == 1:
            counter += 1
        while counter >= K:
            if end_window - start_window + 1 < min_len:
                min_len = end_window - start_window + 1
                start_min = start_window
                end_min = end_window
            frequency_map[array[start_window]] = frequency_map.get(array[start_window]) - 1
            if frequency_map[array[start_window]] == 0:
                counter -= 1
            start_window += 1
        end_window += 1
    if min_len == len(array) + 1:
        print(-1, -1)
    else:
        print(start_min + 1, end_min + 1)


if __name__ == '__main__':
    minimum_segment()
