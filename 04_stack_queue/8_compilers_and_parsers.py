"""
Link: https://www.codechef.com/problems/COMPILER
Time complexity: O(T * N)
Space complexity: O(T * N)
"""


def check_valid(text):
    stack = []
    result = 0
    for i in range(len(text)):
        if text[i] == '<':
            stack.append(text[i])
        else:
            if len(stack) == 0:
                return result
            stack.pop()
            result = i + 1 if len(stack) == 0 else result
    return result


if __name__ == '__main__':
    N = int(input())
    for index in range(N):
        text = input()
        print(check_valid(text))
