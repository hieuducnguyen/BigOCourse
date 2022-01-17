"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 14/12/2021
"""
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        num_list = list(map(int, input().split()))
        result = 0
        for i in range(N):
            frequence = (i + 1) * (N - i)
            if frequence & 1 != 0:
                result ^= num_list[i]
        print(result)
