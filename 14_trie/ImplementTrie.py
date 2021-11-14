"""
Link: https://leetcode.com/problems/implement-trie-prefix-tree/
Time complexity: O(H)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class Node:
    def __init__(self, val, end=False):
        self.val = val
        self.children = {}
        self.end = end


class Trie:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  ## return True
    print(trie.search("app"))  ## return False
    print(trie.startsWith("app"))  ## return True
    trie.insert("app")
    print(trie.search("app"))  ## return True
