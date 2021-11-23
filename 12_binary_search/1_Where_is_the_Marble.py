"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1415
Time complexity: O(T * (N * Log(N) + Q *Log(N)))
Space complexity: O(T * N)
Author: Nguyen Duc Hieu
"""


def lower_bound(key, val_list):
    start, end, mid = 0, len(val_list), 0
    index_key = end
    while start < end:
        mid = (start + end) // 2
        if key <= val_list[mid]:
            end = mid
            index_key = mid
        else:
            start = mid + 1
    return index_key


if __name__ == '__main__':
    test_case = 0
    while True:
        N, Q = map(int, input().split())
        if N == 0:
            break
        val_list = []
        for n in range(N):
            val_list.append(int(input()))
        val_list.sort()
        print("CASE# {}:".format(test_case + 1))
        test_case += 1
        for q in range(Q):
            query = int(input())
            index = lower_bound(query, val_list)
            if index == len(val_list) or val_list[index] != query:
                print("{} not found".format(query))
            else:
                print("{} found at {}".format(query, index + 1))
