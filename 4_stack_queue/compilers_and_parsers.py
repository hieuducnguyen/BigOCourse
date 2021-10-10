"""
Link:
Time complexity: O(n*T)
Space complexity: O(n)
"""


def check_valid(text):
    stack = []
    result = 0
    last_result = 0
    for i in range(len(text)):
        if text[i] == '<':
            stack.append(text[i])
        else:
            if len(stack) == 0:
                return result
            stack.pop()
            result += 2
            if len(stack) == 0:
                last_result = result
    return result if len(stack) == 0 else last_result


if __name__ == '__main__':
    N = int(input())
    for index in range(N):
        text = input()
        print(check_valid(text))
