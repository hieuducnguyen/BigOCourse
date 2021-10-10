"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def check_valid_queue(car_list, car_num):
    tmp_index = 1
    stack = []
    car_index = 0
    while tmp_index <= car_num:
        if car_index >= car_num or car_list[car_index] != tmp_index:
            if len(stack) > 0 and stack[-1] == tmp_index:
                stack.pop()
                tmp_index += 1
            else:
                if car_index >= car_num:
                    break
                stack.append(car_list[car_index])
                car_index += 1
        else:
            car_index += 1
            tmp_index += 1

    return len(stack) == 0


if __name__ == '__main__':
    car_num = int(input())
    while car_num != 0:
        car_list = list(map(int, input().split()))
        if check_valid_queue(car_list, car_num):
            print("yes")
        else:
            print("no")
        car_num = int(input())
    # car_list = [5, 4, 3, 2, 1]
    # print(check_valid_queue(car_list, len(car_list)))
    # car_list = [5, 1, 2, 4, 3]
    # print(check_valid_queue(car_list, len(car_list)))
    # car_list = [4, 5, 1, 2, 3]
    # print(check_valid_queue(car_list, len(car_list)) == False)
    # car_list = [1]
    # print(check_valid_queue(car_list, len(car_list)))
    # car_list = [1, 2]
    # print(check_valid_queue(car_list, len(car_list)))
    # car_list = [4, 1, 5, 2, 3]
    # print(check_valid_queue(car_list, len(car_list)) == False)
    # car_list = [1, 4, 2, 5, 3]
    # print(check_valid_queue(car_list, len(car_list)) == False)
    # car_list = [1, 5, 2, 4, 3]
    # print(check_valid_queue(car_list, len(car_list)))
