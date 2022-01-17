"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 26/12/2021
"""
import math

INF = int(1e10)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({} , {})".format(self.x, self.y)


def distance_func(point_1, point_2):
    return math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)


def bruteforce(points, left, right):
    min_distance = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_distance = min(min_distance, distance_func(points[i], points[j]))
    return min_distance


def strip_min(points, left, right, mid, dis_min):
    split_points = []
    for i in range(left, right):
        if abs(points[i].x - points[mid].x) <= dis_min:
            split_points.append(points[i])
    split_points.sort(key=lambda point: point.y)
    for i in range(len(split_points)):
        for j in range(i + 1, len(split_points)):
            if split_points[j].y - split_points[i].y >= dis_min:
                break
            dis_min = min(dis_min, distance_func(split_points[i], split_points[j]))
    return dis_min


def closest_point(points, left, right):
    if right - left <= 3:
        return bruteforce(points, left, right)
    mid = (left + right) // 2
    min_left = closest_point(points, left, mid)
    min_right = closest_point(points, mid + 1, right)
    dis_min = min(min_left, min_right)
    dis_min = min(dis_min, strip_min(points, left, right, mid, dis_min))
    return dis_min


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        points = []
        for i in range(N):
            x, y = map(int, input().split())
            points.append(Point(x, y))
        points.sort(key=lambda point: point.x)
        closest_distance = closest_point(points, 0, len(points))
        print("{:.4f}".format(closest_distance) if closest_distance < 10000 else "INFINITY")
