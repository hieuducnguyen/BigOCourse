"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""
import heapq
from collections import deque

if __name__ == '__main__':
    output = []
    while True:
        try:
            input_text = input()
        except EOFError as e:
            break
        # input_text = input()
        # if input_text == "0 0":
        #     break
        operation_num = int(input_text)
        structure_list = [True for _ in range(3)]
        stack = []
        queue = deque()
        max_heap = []
        for _ in range(operation_num):
            operate, value = map(int, input().split())
            if operate == 1:
                if structure_list[0]:
                    stack.append(value)
                if structure_list[1]:
                    queue.append(value)
                if structure_list[2]:
                    heapq.heappush(max_heap, -value)
            else:
                if structure_list[0]:
                    if stack.pop() != value:
                        structure_list[0] = False
                if structure_list[1]:
                    if queue.popleft() != value:
                        structure_list[1] = False
                if structure_list[2]:
                    if heapq.heappop(max_heap) != - value:
                        structure_list[2] = False
        # print(structure_list)
        if sum(structure_list) == 0:
            output.append("impossible")
        elif sum(structure_list) > 1:
            output.append("not sure")
        else:
            if structure_list[0]:
                output.append("stack")
            elif structure_list[1]:
                output.append("queue")
            else:
                output.append("priority queue")
    for i in range(len(output)):
        print(output[i])
