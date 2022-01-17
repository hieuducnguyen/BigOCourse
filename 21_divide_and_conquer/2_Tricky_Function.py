"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 26/12/2021
"""

INF = int(1e10)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point_1, point_2):
    return (point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2


def bruteForce(point_list, left, right):
    min_val = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_val = min(min_val, distance(point_list[i], point_list[j]))
    return min_val


def closest(point_list, left, right, mid, min_dis):
    split_point = []
    for i in range(left, right):
        if (mid - i) ** 2 <= min_dis:
            split_point.append(point_list[i])
    split_point.sort(key=lambda point: point.y)
    size = len(split_point)
    for i in range(0, size):
        for j in range(i + 1, size):
            if (split_point[i].y - split_point[j].y) ** 2 >= min_dis:
                break
            min_dis = min(min_dis, distance(split_point[i], split_point[j]))
    return min_dis


def cal_min_val(sum_list, left, right):
    if right - left <= 3:
        return bruteForce(sum_list, left, right)
    mid = (left + right) // 2
    min_left = cal_min_val(sum_list, left, mid)
    min_right = cal_min_val(sum_list, mid + 1, right)
    min_dis = min(min_left, min_right)
    return min(min_dis, closest(sum_list, left, right, mid, min_dis))


if __name__ == '__main__':
    N = int(input())
    input_list = list(map(int, input().split()))
    tmp_sum = 0
    point_list = []
    for i in range(1, N + 1):
        tmp_sum += input_list[i - 1]
        point_list.append(Point(i, tmp_sum))
    print(cal_min_val(point_list, 0, N))
