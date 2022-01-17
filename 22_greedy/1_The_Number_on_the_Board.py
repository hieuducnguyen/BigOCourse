"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 04/01/2022
"""
if __name__ == '__main__':
    K = int(input())
    N = int(input())
    number_list = []
    while N != 0:
        number_list.append(N % 10)
        N //= 10
    number_list.sort(reverse=True)
    total_number = sum(number_list)
    replace_count = 0
    while total_number < K:
        total_number += (9 - number_list[-1])
        number_list.pop()
        replace_count += 1
    print(replace_count)
