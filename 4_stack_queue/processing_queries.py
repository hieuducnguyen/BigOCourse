"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

from queue import Queue

if __name__ == '__main__':
    N, B = map(int, input().split())
    job_queue = Queue()
    time_list = [0] * N
    next_free = 0
    running_id_job = 0
    is_first = True
    for i in range(N):
        ts, run_time = map(int, input().split())
        if job_queue.qsize() < B or next_free <= ts:
            if next_free <= ts:
                if is_first:
                    next_free += (run_time + ts)
                    time_list[i] = next_free
                    is_first = False
                elif job_queue.qsize() > 0:
                    job_decs = job_queue.get()
                    next_free = max(next_free, job_decs[2]) + job_decs[1]
                    time_list[job_decs[0]] = next_free
                    job_queue.put((i, run_time, ts))
                else:
                    next_free = max(next_free, ts) + run_time
                    time_list[i] = next_free
            else:
                job_queue.put((i, run_time, ts))
        else:
            time_list[i] = -1
    while job_queue.qsize() > 0:
        job_decs = job_queue.get()
        next_free += job_decs[1]
        time_list[job_decs[0]] = next_free
    print(' '.join(map(str, time_list)))
