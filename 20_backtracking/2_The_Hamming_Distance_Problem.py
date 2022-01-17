"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 01/01/2022
"""


def count_1(val):
    count = 0
    while val != 0:
        val &= (val - 1)
        count += 1
    return count


if __name__ == '__main__':
    testcase = int(input())
    for t in range(testcase):
        input()
        N, H = map(int, input().split())
        for i in range(1, 2 ** N):
            if count_1(i) == H:
                print(bin(i)[2:].zfill(N))
        if t != testcase - 1:
            print()
