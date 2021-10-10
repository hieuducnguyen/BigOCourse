"""
Link: https://codeforces.com/contest/673/problem/A
Time complexity: O(n)
Space complexity: O(1)
"""


def bear_and_game():
    input()
    cutoff = 15
    for i in map(int, input().split()):
        if i > cutoff:
            break
        else:
            cutoff = i + 15
    return min(cutoff, 90)


if __name__ == '__main__':
    print(bear_and_game())
