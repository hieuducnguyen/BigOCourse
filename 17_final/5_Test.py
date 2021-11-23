"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


class Node:
    def __init__(self, key=""):
        self.key = key
        self.children = dict()
        self.count_word = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, val):
        node = self.root
        not_pass_end_node = False
        for char in val:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
            if node.count_word == 1:
                not_pass_end_node = True
        node.count_word += 1
        return len(node.children) == 0 and not not_pass_end_node


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        trie = Trie()
        result = True
        for n in range(N):
            if result:
                if not trie.add(input()):
                    result = False
            else:
                input()
        if result:
            print("YES")
        else:
            print("NO")
