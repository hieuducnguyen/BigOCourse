"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 21/02/2022
"""
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        increase_list = [1] * N
        decrease_list = [1] * N
        array = [int(input())]
        for n in range(1, N):
            num = int(input())
            max_increase = 1
            max_decrease = 1
            for num_item_ind in range(len(array)):
                if num > array[num_item_ind]:
                    max_decrease = max(max_decrease, decrease_list[num_item_ind] + 1)
                else:
                    max_increase = max(max_increase, increase_list[num_item_ind] + 1)
            increase_list[n] = max_increase
            decrease_list[n] = max_decrease
            array.append(num)
        print(increase_list)
        print(decrease_list)
        print(max(max(increase_list), max(decrease_list)))
