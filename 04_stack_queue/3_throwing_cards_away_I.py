"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1876
Time complexity: O(T * N)
Space complexity: O(T * N)
"""

from collections import deque


def throw_card(N):
    queue = deque([x for x in range(1, N + 1)])
    discard = []
    while len(queue) > 1:
        discard.append(queue.popleft())
        queue.append(queue.popleft())
    remain = queue.popleft()
    if discard:
        print("Discarded cards: %s" % ", ".join(map(str, discard)))
    else:
        print("Discarded cards:")
    print("Remaining card: %d" % remain)


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        throw_card(N)
