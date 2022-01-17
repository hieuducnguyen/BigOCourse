"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 14/12/2021
"""
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, M = map(int, input().split())
        tmp_result = 0
        result_list = []
        k = 0
        while tmp_result < N * M:
            if tmp_result + (N << (k + 1)) <= N * M:
                k += 1
            else:
                result_list.append(k)
                tmp_result += (N << k)
                k = 0
        for i in range(len(result_list)):
            value = result_list[i]
            print("({}<<{})".format(N, value), end="")
            if i != len(result_list) - 1:
                print(" + ", end="")
        print()
