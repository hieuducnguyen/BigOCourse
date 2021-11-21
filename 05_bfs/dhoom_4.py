"""
Link: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/
Time complexity: O(V + E) = O(10^5 + N * 10^5)
Space complexity: O(10^5)
"""

from queue import Queue

MODULAR = 10 ** 5


def bfs(X, target, N, key_list):
    if X % MODULAR == target:
        return 0
    q = Queue()
    visited = [-1 for _ in range(MODULAR + 1)]
    visited[X % MODULAR] = 0
    q.put((X, 0))
    while q.qsize() != 0:
        value = q.get()
        for i in key_list:
            next_value = (value[0] * i) % MODULAR
            if next_value == target:
                return value[1] + 1
            if visited[next_value] < 0:
                visited[next_value] = value[1] + 1
                q.put((next_value, value[1] + 1))
    return -1


if __name__ == '__main__':
    X, target = map(int, input().split())
    N = int(input())
    key_list = list(map(int, input().split()))
    print(bfs(X, target, N, key_list))
