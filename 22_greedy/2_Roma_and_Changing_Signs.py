"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 04/01/2022
"""
import heapq

if __name__ == '__main__':
    N, K = map(int, input().split())
    min_heap = list(map(int, input().split()))
    heapq.heapify(min_heap)
    for i in range(K):
        val = heapq.heappop(min_heap)
        heapq.heappush(min_heap, -val)
    print(sum(min_heap))
