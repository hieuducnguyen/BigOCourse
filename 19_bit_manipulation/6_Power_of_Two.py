"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 15/12/2021
"""


def count_num_bit(number):
    counter = 0
    while number != 0:
        counter += 1
        number &= (number - 1)
    return counter


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        input_list = list(map(int, input().split()))
        sub_set = set()
        result = False
        for val in input_list:
            if count_num_bit(val) == 1:
                print("YES")
                result = True
                break
            new_sub_set = set()
            for sub_val in sub_set:
                new_sub_val = sub_val & val
                if count_num_bit(new_sub_val) == 1:
                    print("YES")
                    result = True
                    break
                new_sub_set.add(new_sub_val)
            sub_set.update(new_sub_set)
            sub_set.add(val)
            if result:
                break
        if not result:
            print("NO")
