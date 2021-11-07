"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import math


def count_citizen(city_list, mid):
    citizen = 0
    for city in city_list:
        if city[3] <= mid:
            citizen += city[2]
    return citizen


if __name__ == '__main__':
    N, S = map(int, input().split())
    city_list = []
    max_distance = 0
    for i in range(N):
        x, y, k = map(int, input().split())
        distance = math.sqrt(x * x + y * y)
        if max_distance < distance:
            max_distance = distance
        city_list.append((x, y, k, distance))
    start, end = 0, max_distance
    key = -1
    while abs(start - end) >= 10 ** (-6):
        mid = (start + end) / 2
        if (S + count_citizen(city_list, mid)) >= 10 ** 6:
            key = mid
            end = mid
        else:
            start = mid
    print("{:.7f}".format(key))
