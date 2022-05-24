"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 13/02/2022
"""
if __name__ == '__main__':
    N, W = map(int, input().split())
    val_list = list(map(int, input().split()))
    pattern_list = list(map(int, input().split()))
    compare_list = [0] * len(val_list)
    compare_pattern_list = [0] * len(pattern_list)
    for i in range(1, len(val_list)):
        compare_list[i] = val_list[i] - val_list[i - 1]
    for i in range(1, len(pattern_list)):
        compare_pattern_list[i] = pattern_list[i] - pattern_list[i - 1]
    print(compare_list)
    print(compare_pattern_list)
