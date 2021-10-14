"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

# if __name__ == '__main__':
#     N = int(input())
#     min_heap = []
#     max_heap = []
#     total = 0
#     prices = []
#     for _ in range(N):
#         input_price = list(map(int, input().split()))
#         total_price = input_price[0]
#         if total_price > 0:
#             add_prices = input_price[1:]
#             for price in add_prices:
#                 index = bisect.bisect(prices, price)
#                 prices.insert(index, price)
#         total += (prices.pop() - prices.pop(0))
#     print(total)
import heapq


class Entry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self > other.value


if __name__ == '__main__':
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
