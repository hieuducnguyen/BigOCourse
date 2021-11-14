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
        self.count_word = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        pass_end_node = False
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
            if node.count_word >= 1:
                pass_end_node = True
        node.count_word += 1
        return len(node.children) == 0 and not pass_end_node


if __name__ == '__main__':
    N = int(input())
    trie = Trie()
    for i in range(N):
        pass_word = input()
        if not trie.add(pass_word):
            print("vulnerable")
            break
    else:
        print("non vulnerable")
