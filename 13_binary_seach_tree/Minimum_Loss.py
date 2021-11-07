"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import bisect

INF = 1e16

if __name__ == '__main__':
    N = int(input())
    input_list = list(map(int, input().split()))
    sorted_list = []
    min_loss = INF
    for val in input_list:
        index = bisect.bisect_right(sorted_list, val)
        if index == len(sorted_list):
            sorted_list.append(val)
        else:
            if min_loss > sorted_list[index] - val:
                min_loss = sorted_list[index] - val
            sorted_list.insert(index, val)
    print(min_loss)
