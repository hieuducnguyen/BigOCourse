"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def method_name(map_value):
    max_value = max(map_value)
    min_value = min(map_value)
    mid_value = 0
    for value in map_value:
        if value != max_value and value != min_value:
            mid_value = value
            break
    return max_value, mid_value, min_value


if __name__ == '__main__':
    map_x = {}
    map_y = {}
    point_list = []
    for i in range(8):
        x, y = map(int, input().split())
        map_x[x] = map_x.get(x, 0) + 1
        map_y[y] = map_y.get(y, 0) + 1
        if [x, y] not in point_list:
            point_list.append([x, y])
    if len(map_x) != 3 or len(map_y) != 3 or len(point_list) != 8:
        print("ugly")
        exit()
    max_x, mid_x, min_x = method_name(map_x)
    max_y, mid_y, min_y = method_name(map_y)
    if [mid_x, mid_y] in point_list:
        print("ugly")
    else:
        print("respectable")
