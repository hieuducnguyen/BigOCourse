"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""
CONST = 1e-7


def equal_amount(midle_energy, energy, K):
    more = 0
    less = 0
    for energy_item in energy:
        if energy_item > midle_energy:
            more += (energy_item - midle_energy)
        else:
            less += (midle_energy - energy_item)
    val = more * (100 - K) / 100 - less
    return val


if __name__ == '__main__':
    N, K = map(int, input().split())
    energy = list(map(int, input().split()))
    energy.sort()
    start, end = 0, 1e10 + 1
    result = -1
    EPSILON = 1e-4
    while start < end:
        mid = (start + end) // 2
        amount = equal_amount(mid * CONST, energy, K)
        if amount == 0:
            result = mid
            print("{:.9f}".format(result * CONST))
            break
        elif amount > 0:
            start = mid + 1
        else:
            end = mid
    else:
        if abs(equal_amount(start * CONST, energy, K)) > abs(equal_amount((start - 1) * CONST, energy, K)):
            print("{:.9f}".format((start - 1) * CONST))
        else:
            print("{:.9f}".format(start * CONST))
