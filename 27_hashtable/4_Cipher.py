"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 15/01/2022
"""
if __name__ == '__main__':
    N, K = map(int, input().split())
    input_list = list(map(int, list(input())))
    new_list = [0]
    result_list = []
    for i in range(N):
        min_dis = min(i, K - 1)
        tmp_xor = 0
        for j in range(min_dis):
            tmp_xor ^= result_list[-1 - j]
        result = tmp_xor ^ input_list[i]
        result_list.append(result)
    print(*result_list, sep="")
