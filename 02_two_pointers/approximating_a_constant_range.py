"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def approximating_a_constant_range():
    len_num = int(input())
    num_list = list(map(int, input().split()))
    queue_max = []
    queue_min = []
    start_window = 0
    end_window = 0
    result = 0
    while end_window < len_num:
        update_queue_max(num_list[end_window], queue_max)
        update_queue_min(num_list[end_window], queue_min)
        while queue_max[0] - queue_min[0] > 1:
            if queue_max[0] == num_list[start_window]:
                queue_max.pop(0)
            if queue_min[0] == num_list[start_window]:
                queue_min.pop(0)
            start_window += 1
        result = max(result, end_window - start_window + 1)
        end_window += 1
    print(result)


def update_queue_min(number, queue_min):
    while len(queue_min) != 0 and queue_min[-1] > number:
        queue_min.pop()
    queue_min.append(number)


def update_queue_max(number, queue_max):
    while len(queue_max) != 0 and queue_max[-1] < number:
        queue_max.pop(-1)
    queue_max.append(number)


if __name__ == '__main__':
    approximating_a_constant_range()
