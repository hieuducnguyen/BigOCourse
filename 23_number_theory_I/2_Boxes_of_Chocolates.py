"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 06/01/2022
"""
if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N, B = map(int, input().split())
        result = 0
        for b in range(B):
            K, *boxes = map(int, input().split())
            tmp_result = 1
            for i in range(K):
                tmp_result = (tmp_result * (boxes[i] % N)) % N
            result = (result + tmp_result) % N
        print(result)
