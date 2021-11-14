"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class Node:
    def __init__(self, key=None):
        self.key = key
        self.children = {}
        self.priority = -1


class Trie:
    def __init__(self):
        self.root = Node()

    def search(self, query):
        node = self.root
        for char in query:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.priority

    def add(self, word, priority):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
            node.priority = max(node.priority, priority)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    trie = Trie()
    for i in range(N):
        word, priority = input().split()
        trie.add(word, int(priority))
    for i in range(Q):
        word_query = input()
        print(trie.search(word_query))
