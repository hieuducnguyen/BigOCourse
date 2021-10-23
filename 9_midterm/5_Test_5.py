"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import heapq

if __name__ == '__main__':
    N = int(input())
    median_index = N // 2
    min_heap = list(map(int, input().split()))
    heapq.heapify(min_heap)
    for i in range(median_index):
        heapq.heappop(min_heap)
    print(min_heap[0])
