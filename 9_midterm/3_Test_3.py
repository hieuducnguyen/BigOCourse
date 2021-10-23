"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    k, n, w = map(int, input().split())
    total = 0
    for i in range(1, w + 1):
        total += k * i
    print(max(0, total - n))
