"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 14/12/2021
"""


def count_1(val):
    count = 0
    while val != 0:
        val &= (val - 1)
        count += 1
    return count


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        friends = []
        for i in range(N):
            friends.append(int(input(), 2))
        result_set = set()
        for i in range(1, 2 ** K):
            enjoy = 0
            for friend in friends:
                if friend & i > 0:
                    enjoy += 1
            if enjoy == N:
                result_set.add(i)
        min_cake = K
        for val in result_set:
            min_cake = min(min_cake, count_1(val))
        print(min_cake)
