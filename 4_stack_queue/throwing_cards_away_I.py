"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

from queue import Queue


def throwCard(N):
    q = Queue()
    for i in range(1, N + 1):
        q.put(i)
    list_throw = []
    while q.qsize() > 1:
        first = q.get()
        list_throw.append(first)
        second = q.get()
        q.put(second)

    return list_throw, q.get() if q.qsize() > 0 else None


if __name__ == '__main__':
    N = int(input())
    while N != 0:
        discard, remain = throwCard(N)
        discard_str = ', '.join(map(str, discard))
        print("Discarded cards:", end="")
        if discard_str:
            print(" " + discard_str)
        else:
            print()
        remain_str = ""
        if remain is not None and remain > 0:
            remain_str = str(remain)
        print("Remaining card: " + remain_str)
        N = int(input())
