"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 27/01/2022
"""


class Person:
    def __init__(self, S, B, i):
        self.S = S
        self.B = B
        self.i = i

    def __lt__(self, other):
        if self.S == other.S:
            return self.B > other.B
        return self.S < other.S


def lower_bound(dp, people, key):
    start = 0
    end = len(dp)
    result = end
    while start < end:
        mid = start + (end - start) // 2
        if people[dp[mid]].B >= key:
            end = mid
            result = mid
        else:
            start = mid + 1
    return result


def LIS(people):
    len_people = len(people)
    path = [-1] * len_people
    dp = [0]
    len_LIS = 1
    start = 0
    for i in range(1, len_people):
        if people[i].B < people[dp[0]].B:
            dp[0] = i
        elif people[i].B > people[dp[-1]].B:
            path[i] = dp[-1]
            dp.append(i)
        else:
            pos = lower_bound(dp, people, people[i].B)
            if pos <= len(dp) - 1:
                path[i] = dp[pos - 1]
                dp[pos] = i
        if len(dp) > len_LIS:
            start = i
            len_LIS = len(dp)
    return path, start


if __name__ == '__main__':
    N = int(input())
    people = []
    for i in range(N):
        S, B = map(int, input().split())
        people.append(Person(S, B, i))
    people.sort()
    len_people = len(people)
    path, start = LIS(people)
    LIS_arr = []
    while start != -1:
        LIS_arr.append(people[start].i + 1)
        start = path[start]
    LIS_arr.reverse()
    print(len(LIS_arr))
    print(*LIS_arr, sep=" ")
