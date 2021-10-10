"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

from queue import Queue


def process_testcase():
    N, T, M = map(int, input().split())
    queue_array = [Queue(), Queue()]
    cur_slide, cur_time = 0, 0
    time_list = [0] * M
    for i in range(M):
        car_info = input()
        ts, slide = int(car_info.split()[0]), car_info.split()[1]
        if slide == 'left':
            queue_array[0].put((i, ts))
        else:
            queue_array[1].put((i, ts))
    waiting = check_waiting(queue_array)
    while waiting > 0:
        if waiting == 1:
            if queue_array[0].qsize() != 0:
                next_time = queue_array[0].queue[0][1]
            else:
                next_time = queue_array[1].queue[0][1]
        else:
            next_time = min(queue_array[0].queue[0][1], queue_array[1].queue[0][1])
        cur_time = max(cur_time, next_time)
        loaded = 0
        while queue_array[cur_slide].qsize() != 0 and queue_array[cur_slide].queue[0][1] <= cur_time and loaded < N:
            loaded += 1
            car_info = queue_array[cur_slide].get()
            time_list[car_info[0]] = cur_time + T
        cur_slide = 1 - cur_slide
        cur_time += T
        waiting = check_waiting(queue_array)
    for _ in range(len(time_list)):
        print(time_list[_])


def check_waiting(queue_array):
    return (queue_array[0].qsize() != 0) + (queue_array[1].qsize() != 0)


if __name__ == '__main__':
    num_testcase = int(input())
    for _ in range(num_testcase):
        process_testcase()
        if _ != num_testcase - 1:
            print()
