"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1415
Time complexity: O(T * (N * Log(N) + Q *Log(N)))
Space complexity: O(T * N)
Author: Nguyen Duc Hieu
"""


def lower_bound(input_list, key):
    left, right, result = 0, len(input_list), len(input_list)
    while left < right:
        mid = (left + right) // 2
        if key <= input_list[mid]:
            right = mid
            result = mid
        else:
            left = mid + 1
    return result


if __name__ == '__main__':
    test_case = 0
    while True:
        N, Q = map(int, input().split())
        if N == 0 and Q == 0:
            break
        test_case += 1
        print("CASE# {}:".format(test_case))
        input_list = []
        for i in range(N):
            input_list.append(int(input()))
        input_list.sort()
        for i in range(Q):
            query_val = int(input())
            # result = bisect.bisect_left(input_list, query_val)
            result = lower_bound(input_list, query_val)
            if result >= len(input_list) or input_list[result] != query_val:
                print("{} not found".format(query_val))
            else:
                print("{} found at {}".format(query_val, result + 1))
