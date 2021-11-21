"""
Link: https://codeforces.com/problemset/problem/691/A
Time complexity: O(N)
Space complexity: O(1)
"""

if __name__ == '__main__':
    print("YES" if min(1, int(input()) - 1) == input().split().count("0") else "NO")
