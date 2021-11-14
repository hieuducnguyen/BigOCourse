"""
Link: https://www.spoj.com/problems/EKO/
Time complexity: O(N * Log(N) + Log(N))
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


def take_woods(mid, woods):
    collect_wood = 0
    for wood in woods:
        if wood > mid:
            collect_wood += (wood - mid)
    return collect_wood


if __name__ == '__main__':
    N, M = map(int, input().split())
    woods = list(map(int, input().split()))
    woods.sort()
    start, end = 0, woods[-1]
    result = 0
    while start < end:
        mid = (start + end) // 2
        wood = take_woods(mid, woods)
        if wood == M:
            print(mid)
            exit()
        elif wood < M:
            end = mid
        else:
            result = mid
            start = mid + 1
    print(result)
