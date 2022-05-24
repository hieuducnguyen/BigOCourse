"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 13/02/2022
"""

INF = int(1e9 + 7)


def pass_cond(mid, sum_t, sum_a, T, A):
    if sum_t[mid] >= T and sum_a[mid] >= A:
        return True
    return False


if __name__ == '__main__':
    C = int(input())
    first = True
    for c in range(C):
        if not first:
            input()
        first = False
        T, A = map(int, input().split())
        N = int(input())
        sum_t = [0] * N
        sum_a = [0] * N
        sum_weight = [0] * N
        t, a, w = map(int, input().split())
        sum_t[0] = t
        sum_a[0] = a
        sum_weight[0] = w
        for n in range(1, N):
            t, a, w = map(int, input().split())
            sum_t[n] = sum_t[n - 1] + t
            sum_a[n] = sum_a[n - 1] + a
            sum_weight[n] = sum_weight[n - 1] + w
        start = 0
        end = N
        result = N - 1
        while start < end:
            mid = start + (end - start) // 2
            if pass_cond(mid, sum_t, sum_a, T, A):
                end = mid
                result = mid
            else:
                start = mid + 1
        print(sum_weight[result])
