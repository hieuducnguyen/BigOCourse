"""
Link: https://www.spoj.com/problems/LAZYPROG/
Time complexity: O(N * log(N))
Space complexity: O(N)
"""
import heapq


class Job:
    def __init__(self, a, b, d):
        self.d = d
        self.b = b
        self.a = a
        self.total_run = 0

    def __lt__(self, other):
        return self.a > other.a

    def set_total_run(self, total_run):
        self.total_run = total_run

    def __str__(self):
        return "Job(a==%s;b==%s;d==%d;total_run==%s)" % (self.a, self.b, self.d, self.total_run)


if __name__ == '__main__':
    num_testcase = int(input())
    for _ in range(num_testcase):
        N = int(input())
        job_list = []
        heap = []
        total = 0
        for i in range(N):
            a, b, d = map(int, input().split())
            job_list.append(Job(a, b, d))
        job_list = sorted(job_list, key=lambda x: (x.d, x.a))
        ts = 0
        for i in range(len(job_list)):
            if ts + job_list[i].b <= job_list[i].d:
                job_list[i].set_total_run(job_list[i].b)
                heapq.heappush(heap, job_list[i])
                ts = ts + job_list[i].b
            else:
                need_time = ts + job_list[i].b - job_list[i].d
                while need_time != 0:
                    if len(heap) > 0 and heap[0].a > job_list[i].a:
                        val = heapq.heappop(heap)
                        if val.total_run >= need_time:
                            need_money = need_time / val.a
                            val.total_run = val.total_run - need_time
                            total += need_money
                            need_time = 0
                            if val.total_run > 0:
                                heapq.heappush(heap, val)
                            job_list[i].set_total_run(job_list[i].b)
                            heapq.heappush(heap, job_list[i])
                        else:
                            need_money = val.total_run / val.a
                            ts -= val.total_run
                            need_time = need_time - val.total_run
                            total += need_money
                    else:
                        need_money = need_time / job_list[i].a
                        total += need_money
                        job_list[i].set_total_run(job_list[i].d - ts)
                        if job_list[i].d - ts > 0:
                            heapq.heappush(heap, job_list[i])
                        need_time = 0
                ts = job_list[i].d
        print("%.2f" % round(total, 2))
