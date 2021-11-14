"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class Node:
    def __init__(self, key=""):
        self.key = key
        self.word_count = 0
        self.children = {}


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

    def check_max_prefix(self, node, len=0):
        count = len * node.word_count
        for child in node.children.values():
            count = max(count, self.check_max_prefix(child, len + 1))
        return count


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        trie = Trie()
        ADN = ""
        for i in range(N):
            ADN = input()
            trie.add(ADN)
        print("Case {}: {}".format(t + 1, trie.check_max_prefix(trie.root)))
