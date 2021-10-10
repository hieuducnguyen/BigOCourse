"""
Link:
Time complexity: O(n)
Space complexity: O(n)
"""


def extend_book():
    N, M = map(int, input().split())
    exam = list(map(int, input().split()))
    prepare = list(map(int, input().split()))
    pointer_exam = len(exam) - 1
    pointer_prepare = len(prepare) - 1
    more_exam = 0
    while pointer_exam >= 0 and pointer_prepare >= 0:
        if exam[pointer_exam] <= prepare[pointer_prepare]:
            pointer_prepare -= 1
        else:
            more_exam += 1
        pointer_exam -= 1

    return more_exam


if __name__ == '__main__':
    print(extend_book())
