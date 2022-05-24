"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 08/02/2022
"""


def can_fill(mid, bottle_list, m):
    tmp_milk = 0
    num_bottle = 0
    for i in range(len(bottle_list)):
        if tmp_milk + bottle_list[i] > mid:
            tmp_milk = bottle_list[i]
            num_bottle += 1
        else:
            tmp_milk += bottle_list[i]
    return num_bottle + 1 <= m


if __name__ == '__main__':
    while True:
        try:
            n, m = map(int, input().split())
            bottle_list = list(map(int, input().split()))
            min_milk = start = min(bottle_list)
            total_milk = end = sum(bottle_list) + 1
            result = end
            while start < end:
                mid = start + (end - start) // 2
                if can_fill(mid, bottle_list, m):
                    result = mid
                    end = mid
                else:
                    start = mid + 1
            print(result)
        except EOFError as EOF:
            break
