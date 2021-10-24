"""
Link:
Time complexity: O(T * N * log(N))
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq
from collections import deque


class Entry:
    def __init__(self, id, priority):
        self.priority = priority
        self.id = id

    def __lt__(self, other):
        return self.priority > other.priority


if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        n, m = map(int, input().split())
        input_list = list(map(int, input().split()))
        entry_list = []
        for j in range(len(input_list)):
            entry_list.append(Entry(j, input_list[j]))
        queue = deque(entry_list)
        max_heap = [x for x in entry_list]
        heapq.heapify(max_heap)
        time = 0
        while True:
            if queue[0].priority == max_heap[0].priority:
                if queue[0].id == m:
                    time += 1
                    break
                else:
                    time += 1
                    queue.popleft()
                    heapq.heappop(max_heap)
            else:
                queue.append(queue.popleft())
        print(time)
