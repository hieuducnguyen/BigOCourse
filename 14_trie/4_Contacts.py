"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class Node:
    def __init__(self, key=""):
        self.key = key
        self.children = {}
        self.word_count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
            node.word_count += 1

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count


if __name__ == '__main__':
    N = int(input())
    trie = Trie()
    for i in range(N):
        operation, name = input().split()
        if operation == "add":
            trie.add(name)
        else:
            print(trie.find(name))
