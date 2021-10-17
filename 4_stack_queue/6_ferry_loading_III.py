"""
Link:
Time complexity: O(T * M) T: testcase, M: num car
Space complexity: O(M)
Author: Nguyen Duc Hieu
"""
from collections import deque


class Car:
    def __init__(self, index, arrive_time):
        self.arrive_time = arrive_time
        self.index = index


def count_time(queue_arr, W, move_time, num_car):
    TS = 0
    side = 0
    arrive_time_result = [0 for _ in range(num_car)]
    while queue_arr[0] or queue_arr[1]:
        if queue_arr[0] and queue_arr[1]:
            TS = max(TS, min(queue_arr[0][0].arrive_time, queue_arr[1][0].arrive_time))
        elif queue_arr[0]:
            TS = max(TS, queue_arr[0][0].arrive_time)
        else:
            TS = max(TS, queue_arr[1][0].arrive_time)
        weight = 0
        while queue_arr[side] and queue_arr[side][0].arrive_time <= TS and weight < W:
            car = queue_arr[side].popleft()
            weight += 1
            arrive_time_result[car.index] = TS + move_time
        TS += move_time
        side = 1 - side
    for car_arrive_time in arrive_time_result:
        print(car_arrive_time)


if __name__ == '__main__':
    C = int(input())
    for i in range(C):
        N, T, M = map(int, input().split())
        queue_arr = [deque(), deque()]
        for j in range(M):
            query = input().split()
            ts = int(query[0])
            side = query[1]
            if side == 'left':
                queue_arr[0].append(Car(j, ts))
            else:
                queue_arr[1].append(Car(j, ts))
        count_time(queue_arr, N, T, M)
        if i != C-1:
            print()
