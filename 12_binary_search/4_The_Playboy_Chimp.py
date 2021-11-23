"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1552
Time complexity: O(N * Log(N) + Q * Log(N))
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


def higher_1(val_list, key):
    if key >= val_list[-1]:
        return -1
    start, end, mid = 0, len(val_list), 0
    result = -1
    while start < end:
        mid = start + (end - start) // 2
        if val_list[mid] <= key:
            start = mid + 1
        else:
            result = mid
            end = mid
    return result


def lower_1(val_list, key):
    if val_list[0] >= key:
        return -1
    start, end, mid = 0, len(val_list), 0
    result = -1
    while start < end:
        mid = start + (end - start) // 2
        if key <= val_list[mid]:
            end = mid
        else:
            result = mid
            start = mid + 1
    return result


def method_1():
    N = int(input())
    height_list = list(map(int, input().split()))
    Q = int(input())
    query_list = list(map(int, input().split()))
    for query in query_list:
        result = lower_1(height_list, query)
        if result != -1:
            print(height_list[result], end=" ")
        else:
            print("X", end=" ")
        result = higher_1(height_list, query)
        if result != -1:
            print(height_list[result])
        else:
            print("X")


def lower_bound(val_list, key):
    start, end, mid = 0, len(val_list), 0
    result = end
    while start < end:
        mid = start + (end - start) // 2
        if key <= val_list[mid]:
            end = mid
            result = mid
        else:
            start = mid + 1
    return result


def upper_bound(val_list, key):
    start, end, mid = 0, len(val_list), 0
    result = end
    while start < end:
        mid = start + (end - start) // 2
        if key < val_list[mid]:
            end = mid
            result = mid
        else:
            start = mid + 1
    return result


def lower(val_list, key):
    if key <= val_list[0]:
        return -1
    return lower_bound(val_list, key) - 1


def higher(val_list, key):
    if val_list[-1] <= key:
        return -1
    return upper_bound(val_list, key)


if __name__ == '__main__':
    # method_1()
    N = int(input())
    height_list = list(map(int, input().split()))
    Q = int(input())
    query_list = list(map(int, input().split()))
    for query in query_list:
        result = lower(height_list, query)
        if result == -1:
            print("X", end=" ")
        else:
            print(height_list[result], end=" ")
        result = higher(height_list, query)
        if result == -1:
            print("X")
        else:
            print(height_list[result])
