"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 28/12/2021
"""


def print_result(result):
    for val in result:
        print(val, end=" ")
    print()


def combination(input_list, N, start, k, tmp_result):
    if k == 0:
        print_result(tmp_result)
        return
    for i in range(start, N):
        tmp_result.append(input_list[i])
        combination(input_list, N, i + 1, k - 1, tmp_result)
        tmp_result.pop()


if __name__ == '__main__':
    is_first = True
    while True:
        N, *input_list = map(int, input().split())
        if N == 0:
            break
        if not is_first:
            print()
        is_first = False
        tmp_result = []
        combination(input_list, N, 0, 6, tmp_result)
