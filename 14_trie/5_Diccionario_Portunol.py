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
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0
        self.count_char = [0] * 26

    def add(self, word):
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                if i > 0:
                    self.count_char[ord(char) - ord('a')] += 1
                node.children[char] = Node(char)
                self.size += 1
            node = node.children[char]
        node.word_count += 1


if __name__ == '__main__':
    while True:
        P, S = map(int, input().split())
        if P == S == 0:
            break
        prefix_trie = Trie()
        suffix_trie = Trie()
        for p in range(P):
            prefix_trie.add(input())
        for s in range(S):
            suffix_trie.add(input()[::-1])
        total_word = prefix_trie.size * suffix_trie.size
        common_word = 0
        for i in range(26):
            common_word += prefix_trie.count_char[i] * suffix_trie.count_char[i]
        print(total_word - common_word)
