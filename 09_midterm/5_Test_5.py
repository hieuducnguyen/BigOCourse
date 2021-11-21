"""
Link: https://vjudge.net/problem/UVA-12100
Author: Nguyen Duc Hieu
"""

import heapq

"""
Time complexity: O(N * Log(N))
Space complexity: O(N)
"""
if __name__ == '__main__':
    N = int(input())
    median_index = N // 2
    min_heap = list(map(int, input().split()))
    min_heap.sort()
    print(min_heap[median_index])

"""
Time complexity: O(N + N/2 * log(N))
Space complexity: O(N)
"""
if __name__ == '__main__':
    N = int(input())
    median_index = N // 2
    min_heap = list(map(int, input().split()))
    heapq.heapify(min_heap)
    for i in range(median_index):
        heapq.heappop(min_heap)
    print(min_heap[0])
