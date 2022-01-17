"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 28/12/2021
"""
import copy


def combination(a, start, N, K, tmp_result, result):
    if len(tmp_result) == K:
        print(*tmp_result, sep=" ")
        result.append(copy.deepcopy(tmp_result))
        return
    for val in a:
        if val not in tmp_result:
            tmp_result.append(val)
            combination(a, start + 1, N, K, tmp_result, result)
            tmp_result.pop()


def combination2(a, start, N, K, tmp_result, result):
    if len(tmp_result) == K:
        print(*tmp_result, sep=" ")
        result.append(copy.deepcopy(tmp_result))
        return
    for i in range(start, N):
        tmp_result.append(a[i])
        combination2(a, i + 1, N, K, tmp_result, result)
        tmp_result.pop()


if __name__ == '__main__':
    N = 5
    K = 3
    a = [1, 2, 3, 4, 5]
    tmp_result = []
    result = []
    combination2(a, 0, N, K, tmp_result, result)
    print(len(result))
