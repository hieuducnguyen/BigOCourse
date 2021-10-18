"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
from collections import deque


class Job:
    def __init__(self, id, arrive_time, execute_time, finish_time=-1):
        self.id = id
        self.execute_time = execute_time
        self.arrive_time = arrive_time
        self.finish_time = finish_time


if __name__ == '__main__':
    n, b = map(int, input())
    job_queue = deque()
    for i in range(n):
        TS, duration = map(int, input().split())
        job_queue.append(Job(i, TS, duration))
    executing_job = None
    TS = 0
    waiting_queue = deque()
    while executing_job is not None or waiting_queue or job_queue:
        next_time = TS
        if executing_job is not None:
            next_time = min(executing_job.finish_time, next_time)
        if waiting_queue:
            next_time = min(waiting_queue[0].arrive_time)
        if job_queue:
            next_time = min(job_queue[0].arrive_time)
        TS = max(TS, next_time)
        # if TS == executing_job.finish_time:
        #     if
