"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


def find_celling(input_list, query, is_lower):
    if is_lower:
        if input_list[0] >= query:
            return "X"
    else:
        if input_list[-1] <= query:
            return "X"
    start, end = 0, len(input_list)
    while start < end:
        mid = (start + end) // 2
        if input_list[mid] == query:
            if is_lower:
                end = mid
            else:
                start = mid + 1
        elif input_list[mid] > query:
            end = mid
        else:
            start = mid + 1

    return input_list[end - 1] if is_lower else input_list[start]


if __name__ == '__main__':
    N = int(input())
    input_list = list(map(int, input().split()))
    Q = int(input())
    query_list = list(map(int, input().split()))
    for query in query_list:
        height_1 = find_celling(input_list, query, True)
        height_2 = find_celling(input_list, query, False)
        print("{} {}".format(height_1, height_2))
