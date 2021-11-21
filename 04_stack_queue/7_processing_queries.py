"""
Link: https://codeforces.com/problemset/problem/644/B
Author: Nguyen Duc Hieu
"""
from collections import deque

INF = int(1e100)


class Job:
    def __init__(self, id, arrive_time, execute_time, finish_time=-1):
        self.id = id
        self.execute_time = execute_time
        self.arrive_time = arrive_time
        self.finish_time = finish_time

    def __str__(self):
        return "Job(id=%s;arrive_time=%s;execute_time=%s)" % (self.id, self.execute_time, self.arrive_time)


"""
Time complexity: O(N)
Space complexity: O(N)
"""


def method_1():
    n, b = map(int, input().split())
    job_queue = deque()
    for i in range(n):
        TS, duration = map(int, input().split())
        job_queue.append(Job(i, TS, duration))
    result = [-1 for _ in range(n)]
    executing_job = None
    TS = 0
    waiting_queue = deque()
    while executing_job is not None or waiting_queue or job_queue:
        next_time = INF
        if executing_job is not None:
            next_time = min(executing_job.finish_time, next_time)
        if job_queue:
            next_time = min(job_queue[0].arrive_time, next_time)
        TS = next_time
        if TS == INF:
            print(TS)
        if executing_job is not None and TS == executing_job.finish_time:
            result[executing_job.id] = TS
            if job_queue and TS == job_queue[0].arrive_time:
                waiting_queue.append(job_queue.popleft())
            executing_job = None
        elif job_queue:
            if len(waiting_queue) < b:
                waiting_queue.append(job_queue.popleft())
            else:
                result[job_queue.popleft().id] = -1
        if waiting_queue and executing_job is None:
            executing_job = waiting_queue.popleft()
            executing_job.finish_time = executing_job.execute_time + TS
    print(*result, sep=" ")


"""
Time complexity: O(N)
Space complexity: O(N)
"""


def method_2():
    n, b = map(int, input().split())
    processing = 0
    queue = deque()
    for _ in range(n):
        arrive_time, duration = map(int, input().split())
        while queue and arrive_time >= queue[0]:
            queue.popleft()
        if len(queue) <= b:
            processing = max(processing, arrive_time) + duration
            queue.append(processing)
            print(processing, end=" ")
        else:
            print(-1, end=" ")


if __name__ == '__main__':
    method_2()
