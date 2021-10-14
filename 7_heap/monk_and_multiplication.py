"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""
import heapq


class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


if __name__ == '__main__':
    N = int(input())
    input_list = list(map(int, input().split()))
    heap = []
    for i in range(len(input_list)):
        heapq.heappush(heap, PQEntry(input_list[i]))
        if i < 2:
            print(-1)
        else:
            pre_pre = heapq.heappop(heap)
            pre = heapq.heappop(heap)
            print(pre_pre.value * pre.value * heap[0].value)
            heapq.heappush(heap, pre_pre)
            heapq.heappush(heap, pre)
