"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import bisect

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
            result = bisect.bisect_left(input_list, query_val)
            if result >= len(input_list) or input_list[result] != query_val:
                print("{} not found".format(query_val))
            else:
                print("{} found at {}".format(query_val, result + 1))
