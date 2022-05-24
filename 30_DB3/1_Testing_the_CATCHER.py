"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 25/01/2022
"""


def lower_bound(dp, input_list, key):
    start = 0
    end = len(dp)
    result = start
    while start < end:
        mid = start + (end - start) // 2
        if input_list[dp[mid]] < key:
            end = mid
            result = mid
        else:
            start = mid + 1
    return result


def LDS(input_list):
    dp = [0]
    for i in range(1, len(input_list)):
        if input_list[dp[0]] < input_list[i]:
            dp[0] = i
        elif input_list[dp[-1]] >= input_list[i]:
            dp.append(i)
        else:
            pos = lower_bound(dp, input_list, input_list[i])
            dp[pos] = i
    return len(dp)


# if __name__ == '__main__':
#     input_list = [4, 3, 87, 1, 3, 2]
#     print(LDS(input_list))

if __name__ == '__main__':
    num_test = 1
    first = True
    while True:
        val = int(input())
        if val == -1:
            break
        if not first:
            print()
        first = False
        input_list = [val]
        while True:
            val = int(input())
            if val == -1:
                break
            input_list.append(val)
        len_LDS = LDS(input_list)
        print("Test #{}:".format(num_test))
        num_test += 1
        print("  maximum possible interceptions: {}".format(len_LDS))
