"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 02/01/2022
"""
first_num = 1431655765
second_num = 2863311530

if __name__ == '__main__':
    while True:
        num = int(input())
        if num == 0:
            break
        num_1, num_2 = 0, 0
        first = True
        for i in range(32):
            if (1 << i) & num > 0:
                if first:
                    num_1 |= 1 << i
                else:
                    num_2 |= 1 << i
                first = not first
        print(num_1, num_2)
