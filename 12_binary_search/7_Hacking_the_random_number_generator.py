"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import bisect

if __name__ == '__main__':
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list.sort()
    counter = 0
    for i in range(len(input_list)):
        search_val = input_list[i] + M
        index_val = bisect.bisect_left(input_list, search_val, i + 1, len(input_list))
        if index_val < len(input_list) and input_list[index_val] == search_val:
            counter += 1
    print(counter)
