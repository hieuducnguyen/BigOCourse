"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
from collections import deque


def next_word(text_1, text_2):
    diff = 0
    for u in range(len(text_1)):
        if text_1[u] != text_2[u]:
            diff += 1
            if diff > 1:
                return False
    return True


def build_grap(len_map, word_id_map):
    num_word = len(word_id_map)
    graph = [[] for i in range(num_word)]
    for length in len_map.keys():
        word_list = len_map[length]
        word_list.sort()
        num_same_len_word = len(word_list)
        for j in range(num_same_len_word):
            for k in range(j + 1, num_same_len_word):
                if next_word(word_list[j], word_list[k]):
                    graph[word_id_map[word_list[j]]].append(word_id_map[word_list[k]])
                    graph[word_id_map[word_list[k]]].append(word_id_map[word_list[j]])
    return graph


def bfs(start, end, graph):
    visited = [-1 for _ in range(len(graph))]
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        u = queue.popleft()
        if u == end:
            break
        for v in graph[u]:
            if visited[v] < 0:
                visited[v] = visited[u] + 1
                queue.append(v)
    return visited[end]


if __name__ == '__main__':
    N = int(input())
    input()
    for i in range(N):
        len_map = {}
        word_id_map = {}
        for k in range(1, 11):
            len_map[k] = []
        index = 0
        while True:
            text = input()
            if text == "*":
                break
            len_map[len(text)].append(text)
            word_id_map[text] = index
            index += 1
        graph = build_grap(len_map, word_id_map)
        # print(graph)
        while True:
            try:
                input_text = input()
            except EOFError as e:
                break
            if input_text == "":
                break
            word_1, word_2 = input_text.split()
            distance = bfs(word_id_map[word_1], word_id_map[word_2], graph)
            print("%s %s %s" % (word_1, word_2, distance))
