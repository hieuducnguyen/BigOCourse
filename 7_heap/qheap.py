import bisect
import heapq

"""
Link: https://www.hackerrank.com/challenges/qheap1/problem
Time complexity: O(N * N) // because insert and remove in list required O(N)
Space complexity: O(N)
N : num value
"""


# not recommend
def method_1():
    Q = int(input())
    sorted_list = []
    for _ in range(Q):
        query = input()
        if query == "3":
            print(sorted_list[0])
        else:
            opt, v = map(int, query.split())
            if opt == 1:
                bin_index = bisect.bisect(sorted_list, v)
                if bin_index < len(sorted_list) and sorted_list[bin_index] == v:
                    continue
                else:
                    sorted_list.insert(bin_index, v)
            else:
                bin_index = bisect.bisect(sorted_list, v)
                if bin_index - 1 < len(sorted_list) and sorted_list[bin_index - 1] == v:
                    sorted_list.pop(bin_index - 1)


"""
Time complexity: O(N * log(N))
Space complexity: O(N)
"""


def method_2():
    Q = int(input())
    min_heap = []
    dict = {}
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            val = int(query[1])
            heapq.heappush(min_heap, val)
            dict[val] = dict.get(val, 0) + 1
        elif query[0] == "2":
            val = int(query[1])
            dict[val] -= 1
            while len(min_heap) > 0 and dict[min_heap[0]] == 0:
                heapq.heappop(min_heap)
        else:
            print(min_heap[0])


if __name__ == '__main__':
    method_2()
