"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 04/01/2022
"""
if __name__ == '__main__':
    N = int(input())
    input_list = list(map(int, input().split()))
    input_list.sort()
    diff = 0
    for i in range(1, N + 1):
        diff += abs(input_list[i - 1] - i)
    print(diff)
