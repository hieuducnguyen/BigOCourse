"""
Link: 
Time complexity: O(n)
Space complexity: O(n)
"""


def dress_in_vest():
    M, N, X, Y = map(int, input().split())
    soldiers = list(map(int, input().split()))
    vests = list(map(int, input().split()))
    pointer_soldier = 0
    pointer_vest = 0
    output = []
    while pointer_vest < len(vests) and pointer_soldier < len(soldiers):
        if soldiers[pointer_soldier] - X <= vests[pointer_vest] <= soldiers[pointer_soldier] + Y:
            output.append([pointer_soldier + 1, pointer_vest + 1])
            pointer_soldier += 1
            pointer_vest += 1
        elif vests[pointer_vest] > soldiers[pointer_soldier] + Y:
            pointer_soldier += 1
        else:
            pointer_vest += 1
    print(len(output))
    for i in output:
        print(i[0], i[1])


if __name__ == '__main__':
    dress_in_vest()
