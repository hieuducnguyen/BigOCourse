"""
Link: https://codeforces.com/problemset/problem/295/B
Time complexity: O(N^3)
Space complexity: O(N^2)
Author: Nguyen Duc Hieu
"""

INF = int(1e10)

if __name__ == '__main__':
    N = int(input())
    max_trix = []
    for n in range(N):
        max_trix.append(list(map(int, input().split())))
    remove_list = list(map(lambda x: int(x) - 1, input().split()))
    add_list = remove_list[::-1]
    result = []
    for k in range(len(add_list)):
        vertex = add_list[k]
        for i in range(N):
            for j in range(N):
                if max_trix[i][j] > max_trix[i][vertex] + max_trix[vertex][j]:
                    max_trix[i][j] = max_trix[i][vertex] + max_trix[vertex][j]
        total = 0
        for i in add_list[:k + 1]:
            for j in add_list[:k + 1]:
                total += max_trix[i][j]
        result.append(total)
    result.reverse()
    print(*result, sep=" ")
