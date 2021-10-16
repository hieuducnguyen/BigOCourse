"""
Link:
"""
import heapq


class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


"""
Time complexity: O(N * log(N))
Space complexity: O(N)
"""


def method_1():
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


"""
Time complexity: O(N * 8 * log(3)) ~~ O(N)
Space complexity: O(N)
"""


def method_2():
    N = int(input())
    input_list = list(map(int, input().split()))
    min_heap = []
    for i in range(N):
        heapq.heappush(min_heap, input_list[i])
        if len(min_heap) > 2:
            if len(min_heap) > 3:
                heapq.heappop(min_heap)
            val_1 = heapq.heappop(min_heap)
            val_2 = heapq.heappop(min_heap)
            val_3 = heapq.heappop(min_heap)
            print(val_1 * val_2 * val_3)
            heapq.heappush(min_heap, val_1)
            heapq.heappush(min_heap, val_2)
            heapq.heappush(min_heap, val_3)
        else:
            print(-1)


"""
Time complexity: O(N)
Space complexity: O(N)
"""


def method_3():
    N = int(input())
    input_list = list(map(int, input().split()))
    max_1 = max_2 = max_3 = -1
    for i in range(N):
        if input_list[i] >= max_3:
            max_1 = max_2
            max_2 = max_3
            max_3 = input_list[i]
        elif max_2 <= input_list[i] < max_3:
            max_1 = max_2
            max_2 = input_list[i]
        elif max_1 <= input_list[i] < max_2:
            max_1 = input_list[i]
        if i >= 2:
            print(max_3 * max_2 * max_1)
        else:
            print(-1)


if __name__ == '__main__':
    method_3()
