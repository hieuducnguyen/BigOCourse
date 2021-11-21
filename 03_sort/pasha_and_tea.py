"""
Link:
Time complexity: O(nlog(n))
Space complexity: O(n)
"""

if __name__ == '__main__':
    n, w = map(int, input().split())
    tea_list = list(map(int, input().split()))
    tea_list.sort()
    print(min(w / (3 * n), tea_list[0], tea_list[n] / 2) * 3 * n)
