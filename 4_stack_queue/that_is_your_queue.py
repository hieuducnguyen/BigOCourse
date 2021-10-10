"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


class Node:
    def __init__(self, data, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next


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
        ll = LinkedList()
        print("Case " + str(index_test_case) + ":")
        map_node = {}
        for i in range(1, min(P + 1, 1001)):
            node = Node(i)
            ll.addEnd(node)
            map_node[i] = node
        for i in range(C):
            text = input()
            if text == 'N':
                node = ll.removeHead()
                print(node.data)
                ll.addEnd(node)
            else:
                emergency = int(text.split()[1])
                if emergency in map_node:
                    need_remove = map_node[emergency]
                    ll.remove(need_remove)
                    ll.addHead(need_remove)
                else:
                    new_node = Node(emergency)
                    map_node[emergency] = new_node
                    ll.addHead(new_node)
            # ll.print()
        ll.removeAll()
        index_test_case += 1
        P, C = map(int, input().split())
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # ll = LinkedList()
    # ll.addEnd(node1)
    # ll.print()
    # ll.addEnd(node2)
    # ll.print()
    # ll.addEnd(node3)
    # ll.print()
    # ll.remove(node2)
    # ll.print()
    # ll.addHead(node2)
    # ll.print()
    # ll.remove(node1)
    # ll.print()
    # ll.addEnd(node1)
    # ll.print()
    # node = ll.removeHead()
    # ll.addEnd(node)
    # ll.print()
    # ll.removeAll()
    # ll.print()
    # print("end")
    # list = list(range(1, 125660017))
    # print("create finish")
    # list.remove(96166769)
    # print("create remove")
    # list.insert(0, 96166769)
    # print("create insert")
    # print(list.pop(0))
    # print("create pop")
