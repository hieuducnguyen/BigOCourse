"""
Link: https://www.codechef.com/problems/RRATING
"""
import heapq

"""
Time complexity: O(N * log(N))
Space complexity: O(N)
"""


def method_1():
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


"""
Time complexity: O(N * log(N))
Space complexity: O(N)
"""


def method_2():
    N = int(input())
    min_heap = []
    max_heap = []
    size_post = 0
    for _ in range(N):
        query = input()
        if query == "2":
            if size_post > 2:
                print(min_heap[0])
            else:
                print("No reviews yet")
        else:
            op, val_string = query.split()
            val = int(val_string)
            size_post += 1
            if size_post == 1:
                heapq.heappush(max_heap, -val)
                continue
            if - max_heap[0] >= val:
                heapq.heappush(max_heap, -val)
            else:
                heapq.heappush(min_heap, val)
            if len(min_heap) < size_post // 3:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > size_post // 3:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))


if __name__ == '__main__':
    method_2()
