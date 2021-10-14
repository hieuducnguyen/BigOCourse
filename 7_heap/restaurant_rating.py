"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""
import heapq

if __name__ == '__main__':
    N = int(input())
    min_heap_top = []
    max_heap_remain = []
    size_post = 0
    for _ in range(N):
        input_text = input()
        if input_text == "2":
            if size_post < 3:
                print("No reviews yet")
            else:
                print(-max_heap_remain[0])

        else:
            operation, value = map(int, input_text.split())
            size_post += 1
            if len(max_heap_remain) > 2:
                if -max_heap_remain[0] > value:
                    heapq.heappush(max_heap_remain, -value)
                else:
                    heapq.heappush(min_heap_top, value)
                while len(min_heap_top) > size_post // 3 - 1:
                    pop_value = heapq.heappop(min_heap_top)
                    heapq.heappush(max_heap_remain, - pop_value)
                while len(min_heap_top) < size_post // 3 - 1:
                    pop_value = heapq.heappop(max_heap_remain)
                    heapq.heappush(min_heap_top, - pop_value)
            else:
                heapq.heappush(max_heap_remain, -value)
