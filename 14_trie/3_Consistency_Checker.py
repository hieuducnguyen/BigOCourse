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
        pass_end_node = False
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
            if node.word_count >= 1:
                pass_end_node = True
        node.word_count += 1
        return len(node.children) == 0 and not pass_end_node


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        trie = Trie()
        consistent = True
        for i in range(N):
            phone_num = input()
            if consistent:
                consistent = trie.add(phone_num)
        print("Case {}: {}".format(t + 1, "YES" if consistent else "NO"))
