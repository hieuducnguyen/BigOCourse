"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1895
Time complexity: O(N + N * Log(N))
Space complexity: O(N)
"""
import heapq

if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        input_list = list(map(int, input().split()))
        if len(input_list) <= 2:
            print(sum(input_list))
            continue
        heapq.heapify(input_list)
        print_value = 0
        while len(input_list) != 1:
            min_value_1 = heapq.heappop(input_list)
            min_value_2 = heapq.heappop(input_list)
            sum_value = min_value_1 + min_value_2
            heapq.heappush(input_list, sum_value)
            print_value += sum_value
        print(print_value)
