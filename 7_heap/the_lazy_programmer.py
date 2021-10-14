"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""

if __name__ == '__main__':
    num_testcase = int(input())
    for _ in range(num_testcase):
        N = int(input())
        total = 0
        for i in range(N):
            a, b, d = map(int, input().split())
            extend = (b - d) / a
            if extend > 0:
                total += extend
        print("%.2f" % total)
