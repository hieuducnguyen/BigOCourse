"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


class Node:
    def __init__(self, data, real, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next
        self.real = real


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addEnd(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = None
            self.tail.next = None
            self.tail.pre = None
            self.head.pre = None
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None

    def addHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = None
            self.tail.next = None
            self.tail.pre = None
            self.head.pre = None
        else:
            self.head.pre = node
            node.next = self.head
            self.head = node
            self.head.pre = None

    def remove(self, node):
        if self.head is node and self.tail is node:
            self.head, self.tail = None, None
        elif self.head is node:
            self.head = self.head.next
            self.head.pre = None
        elif self.tail is node:
            self.tail = self.tail.pre
            self.tail.next = None
        else:
            node.pre.next, node.next.pre = node.next, node.pre
        node.pre, node.next = None, None
        return node

    def removeHead(self):
        if self.head is None:
            return None
        else:
            removed_node = self.remove(self.head)
            return removed_node

    def removeAll(self):
        temp = self.head
        while temp:
            self.remove(temp)
            temp = self.head
        temp = None

    def print(self):
        node = self.head
        while node is not None:
            print(node.data, end=", ")
            node = node.next
        print()


if __name__ == '__main__':
    P, C = map(int, input().split())
    index_test_case = 1
    while P != 0 and C != 0:
        print("Case " + str(index_test_case) + ":")
        preValue = -1
        ll = LinkedList()
        change_set = set()
        for i in range(C):
            text = input()
            if text == 'N':
                if ll.head is not None and ll.head.data == preValue:
                    for _ in range(2):
                        tmp_head = ll.removeHead()
                        ll.addEnd(tmp_head)
                    print(ll.head.data + 1)
                else:
                    preValue += 1
                    while preValue in change_set:
                        preValue += 1
                    preValue %= P
                    print(preValue + 1)
            else:
                emergency = int(text.split()[1])
                change_set.add(emergency - 1)
                node = Node(emergency - 1, True)
                fake = Node(preValue, False)
                ll.addHead(node)
                ll.addHead(fake)
        index_test_case += 1
        P, C = map(int, input().split())
