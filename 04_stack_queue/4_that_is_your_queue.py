"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=3359
Time complexity: O(T * (E * N))
Space complexity: O(T * N)
Author: Nguyen Duc Hieu
"""
from collections import deque

if __name__ == '__main__':
    num_test = 0
    while True:
        P, C = map(int, input().split())
        if P == 0 and C == 0:
            break
        num_test += 1
        print("Case %s:" % num_test)
        size_queue = min(P, C)
        queue = deque([x for x in range(1, size_queue + 1)])
        for i in range(C):
            query = input()
            if query == "N":
                val = queue.popleft()
                print(val)
                queue.append(val)
            else:
                op, val_string = query.split()
                val = int(val_string)
                for _ in range(len(queue)):
                    if queue[0] != val:
                        queue.append(queue.popleft())
                    else:
                        queue.popleft()
                queue.appendleft(val)
