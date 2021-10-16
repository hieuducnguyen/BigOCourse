"""
Link: https://www.spoj.com/problems/PRO/
"""

import heapq

'''
Time complexity: O(N * log(N)) when length head > 2 * N and O(N * N) when length heap < 2 * N
Space complexity: O(N)
'''


def method_1():
    N = int(input())
    min_heap = []
    max_heap = []
    total = 0
    for _ in range(N):
        input_price = list(map(int, input().split()))
        total_price = input_price[0]
        for i in range(1, total_price + 1):
            heapq.heappush(min_heap, input_price[i])
            heapq.heappush(max_heap, -input_price[i])
        min_value = heapq.heappop(min_heap)
        max_value = heapq.heappop(max_heap)
        total += (- max_value - min_value)
        if (len(min_heap) < 2 * N):
            min_heap.remove(-max_value)
            max_heap.remove(-min_value)
            heapq.heapify(min_heap)
            heapq.heapify(max_heap)
    print(total)


'''
Time complexity: O(N * log(N))
Space complexity: O(N)
'''


def method_2():
    N = int(input())
    min_heap = []
    remove_min_heap = []
    max_heap = []
    remove_max_heap = []
    total = 0
    for _ in range(N):
        input_price = list(map(int, input().split()))
        total_price = input_price[0]
        for i in range(1, total_price + 1):
            heapq.heappush(min_heap, input_price[i])
            heapq.heappush(max_heap, -input_price[i])
        min_val = heapq.heappop(min_heap)
        max_val = -heapq.heappop(max_heap)
        total += (max_val - min_val)
        heapq.heappush(remove_min_heap, max_val)
        heapq.heappush(remove_max_heap, -min_val)
        while len(remove_max_heap) > 0 and remove_max_heap[0] == max_heap[0]:
            heapq.heappop(remove_max_heap)
            heapq.heappop(max_heap)
        while len(remove_min_heap) > 0 and remove_min_heap[0] == min_heap[0]:
            heapq.heappop(remove_min_heap)
            heapq.heappop(min_heap)
    print(total)


if __name__ == '__main__':
    method_2()
