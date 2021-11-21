"""
Link:
Time complexity: O(nlog(n))
Space complexity: O(n)
"""

if __name__ == '__main__':
    k = int(input())
    months = list(map(int, input().split()))
    months.sort(reverse=True)
    tree_tall = 0
    work_month = 0
    while tree_tall < k and work_month < 12:
        tree_tall += months[work_month]
        work_month += 1
    if tree_tall == k:
        print(work_month)
    else:
        print(-1)
