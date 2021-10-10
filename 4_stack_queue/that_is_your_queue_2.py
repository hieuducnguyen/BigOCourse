"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

if __name__ == '__main__':
    P, C = map(int, input().split())
    index_test_case = 1
    while P != 0 and C != 0:
        print("Case " + str(index_test_case) + ":")
        ll = list(range(1, P + 1))
        for i in range(C):
            text = input()
            if text == 'N':
                head = ll.pop(0)
                print(head)
                ll.append(head)
            else:
                emergency = int(text.split()[1])
                ll.remove(emergency)
                ll.insert(0, emergency)
            # print(ll)
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
