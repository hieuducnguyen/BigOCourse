"""
Link: https://codeforces.com/problemset/problem/37/C
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import sys

sys.setrecursionlimit(10 ** 3 + 5)


class Node:
    def __init__(self, key=-1):
        self.key = key
        self.children = {}
        self.count_word = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, root, level, length, prefix):
        if level == length and len(root.children) == 0:
            root.count_word += 1
            return True, prefix
        if level > length:
            return False, None
        node = root
        for i in range(2):
            if i not in node.children:
                node.children[i] = Node(i)
            node = node.children[i]
            if node.count_word >= 1:
                continue
            add_result = self.add(node, level + 1, length, prefix + str(i))
            if add_result[0]:
                return add_result
        return False, None


if __name__ == '__main__':
    N = int(input())
    result = []
    trie = Trie()
    len_text_arr = list(map(int, input().split()))
    for len_txt in len_text_arr:
        result_add = trie.add(trie.root, 0, len_txt, "")
        if not result_add[0]:
            print("NO")
            break
        else:
            result.append(result_add[1])
    else:
        print("YES")
        for k in range(len(result)):
            print(result[k])
