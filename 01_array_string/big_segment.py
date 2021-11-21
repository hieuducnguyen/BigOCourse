"""
Link: https://codeforces.com/contest/242/problem/B
Time complexity: O(n)
Space complexity: O(n)
"""


def check_bigsegment():
    num_bigsegment = int(input())
    big_segment_list = []
    min, max = None, None
    for i in range(num_bigsegment):
        big_segment = list(map(int, input().split()))
        if min is None or min > big_segment[0]:
            min = big_segment[0]
        if max is None or max < big_segment[1]:
            max = big_segment[1]
        big_segment_list.append(big_segment)
    if [min, max] in big_segment_list:
        print(big_segment_list.index([min, max]) + 1)
    else:
        print(-1)


if __name__ == '__main__':
    check_bigsegment()
