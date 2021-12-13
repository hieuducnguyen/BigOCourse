"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 11/12/2021
"""
import heapq

if __name__ == '__main__':
    test_case = 1
    while True:
        try:
            N = int(input())
            list_item = []
            for i in range(N):
                list_item.append(input())
            M = int(input())
            graph = [[] for _ in range(N)]
            indegrees = [0] * N
            for i in range(M):
                first, second = input().split()
                graph[list_item.index(first)].append(list_item.index(second))
                indegrees[list_item.index(second)] += 1
            min_heap = []
            for i in range(N):
                if indegrees[i] == 0:
                    heapq.heappush(min_heap, i)
            orderings = []
            while min_heap:
                src = heapq.heappop(min_heap)
                orderings.append(src)
                for adjacency in graph[src]:
                    indegrees[adjacency] -= 1
                    if indegrees[adjacency] == 0:
                        heapq.heappush(min_heap, adjacency)
            order_drink = []
            for i in orderings:
                order_drink.append(list_item[i])
            print(
                "Case #{}: Dilbert should drink beverages in this order: {}.".format(test_case, " ".join(order_drink)))
            print()
            test_case += 1
            input()
        except EOFError:
            break
