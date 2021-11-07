"""
Source: BigO
Time complexity: O(T * (10 * V^2 + M * (V + E)))
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
from collections import deque


def is_next_word(word_1, word_2):
    diff = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            diff += 1
            if diff > 1:
                break
    return diff == 1


def bfs(source_id, dest_id, graph):
    dist = [-1] * len(graph)
    queue = deque([source_id])
    dist[source_id] = 0
    while queue:
        source = queue.popleft()
        if source == dest_id:
            break
        for adjacency in graph[source]:
            if dist[adjacency] < 0:
                dist[adjacency] = dist[source] + 1
                queue.append(adjacency)
    return dist[dest_id]


if __name__ == '__main__':
    T = int(input())
    input()
    for i in range(T):
        list_word = []
        while True:
            input_text = input()
            if input_text == "*":
                break
            list_word.append(input_text)
        graph = [[] for _ in range(len(list_word))]
        for u in range(len(list_word)):
            for v in range(u + 1, len(list_word)):
                if len(list_word[u]) == len(list_word[v]):
                    if is_next_word(list_word[u], list_word[v]):
                        graph[u].append(v)
                        graph[v].append(u)
        while True:
            input_query = ""
            try:
                input_query = input()
            except EOFError:
                exit()
            if input_query == "":
                break
            source, dest = input_query.split()
            source_id = list_word.index(source)
            dest_id = list_word.index(dest)
            cost = bfs(source_id, dest_id, graph)
            print("{} {} {}".format(source, dest, cost))
