"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 02/01/2022
"""
import sys

sys.setrecursionlimit(10 ** 4)


def count_paint(height_list, N):
    min_height = min(height_list)
    new_height_list = []
    have_higher = False
    num_paint = 0
    for i in range(N):
        if height_list[i] - min_height > 0:
            new_height_list.append(height_list[i] - min_height)
            have_higher = True
        if (height_list[i] - min_height == 0 or i == N - 1) and have_higher:
            num_paint += count_paint(new_height_list, len(new_height_list))
            new_height_list.clear()
            have_higher = False
    return min(min_height + num_paint, N)


if __name__ == '__main__':
    N = int(input())
    height_list = list(map(int, input().split()))
    print(count_paint(height_list, N))
