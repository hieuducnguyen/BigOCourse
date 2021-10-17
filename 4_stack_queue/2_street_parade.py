"""
Link: https://www.spoj.com/problems/STPAR/
"""

from collections import deque

"""
Time complexity: O(T * N) T: testcase, N: num car in each testcase
Space complexity: O(T * N)
"""


def method_1():
    while True:
        num_car = int(input())
        if num_car == 0:
            break
        input_car = list(map(int, input().split()))
        queue = deque(input_car)
        stack = []
        next_car_index = 1
        while queue or stack:
            if queue and queue[0] == next_car_index:
                queue.popleft()
                next_car_index += 1
            elif stack and stack[-1] == next_car_index:
                stack.pop()
                next_car_index += 1
            elif queue:
                stack.append(queue.popleft())
            else:
                print("no")
                break
        else:
            print("yes")


if __name__ == '__main__':
    method_1()
