"""
Link: https://www.spoj.com/problems/ONP/
Author: Nguyen Duc Hieu
"""

operator_set = {'+', '-', '*', '/', '^'}

"""
Time complexity: O(T * N)
Space complexity: O(N)
"""


def transform_1(expression):
    stack = []
    for i in expression:
        if i == '(':
            continue
        elif i.isalpha() or i in operator_set:
            stack.append(i)
        elif i == ')':
            tmp = []
            for _ in range(3):
                tmp.append(stack.pop())
            stack.append(tmp[2] + tmp[0] + tmp[1])
    return "".join(stack)


"""
Time complexity: O(T * N)
Space complexity: O(N)
"""


def transform_2(expression):
    stack = []
    for symbol in expression:
        if symbol.isalpha():
            print(symbol, end='')
        elif symbol == ')':
            print(stack.pop(), end='')
        elif symbol != '(':
            stack.append(symbol)
    print()


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        expression = input()
        # result = transform_1(expression)
        # print(result)
        transform_2(expression)
