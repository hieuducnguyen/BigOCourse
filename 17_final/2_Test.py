"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""


def func(x):
    return x * (x - 1) + 1


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        val = int(input())
        start, end, mid = 0, 10 ** 15 + 1, 0
        while start < end:
            mid = start + (end - start) // 2
            if val <= func(mid):
                result = mid
                end = mid
            else:
                start = mid + 1
        if val == func(mid):
            print("Case {}: {} {}".format(t + 1, mid, mid))
            continue
        if func(result) - result + 1 > val:
            result -= 1
        if result % 2 == 0:
            if func(result) - result + 1 <= val <= func(result):
                start, end = 0, result + 1
                while start < end:
                    mid = start + (end - start) // 2
                    temp = func(result) - result + 1 + mid
                    if temp == val:
                        print("Case {}: {} {}".format(t + 1, mid + 1, result))
                        break
                    elif temp > val:
                        end = mid
                    else:
                        start = mid + 1
            else:
                start, end = 0, result + 1
                while start < end:
                    mid = start + (end - start) // 2
                    temp = func(result) + mid
                    if temp == val:
                        print("Case {}: {} {}".format(t + 1, result, result - mid))
                        break
                    elif temp > val:
                        end = mid
                    else:
                        start = mid + 1
        else:
            if func(result) - result + 1 <= val <= func(result):
                start, end = 0, result + 1
                while start < end:
                    mid = start + (end - start) // 2
                    temp = func(result) - result + 1 + mid
                    if temp == val:
                        print("Case {}: {} {}".format(t + 1, result, mid + 1))
                        break
                    elif temp > val:
                        end = mid
                    else:
                        start = mid + 1
            else:
                start, end = 0, result + 1
                while start < end:
                    mid = start + (end - start) // 2
                    temp = func(result) + mid
                    if temp == val:
                        print("Case {}: {} {}".format(t + 1, result - mid, result))
                        break
                    elif temp > val:
                        end = mid
                    else:
                        start = mid + 1
