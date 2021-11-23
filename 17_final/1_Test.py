"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
import copy

if __name__ == '__main__':
    N = int(input())
    input_list = list(map(int, input().split()))
    entry_list = []
    for i in range(len(input_list)):
        entry_list.append((input_list[i], i))
    entry_list.sort()
    result = []
    result.append(copy.deepcopy(entry_list))
    for i in range(N - 1, 0, -1):
        if entry_list[i][0] == entry_list[i - 1][0]:
            new_list = copy.deepcopy(entry_list)
            new_list[i], new_list[i - 1] = new_list[i - 1], new_list[i]
            result.append(new_list)
        if len(result) == 3:
            break
    if len(result) == 3:
        print("YES")
        for i in range(3):
            print(*list(map(lambda x: x[1] + 1, result[i])), sep=" ")
    else:
        print("NO")
