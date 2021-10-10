"""
Link:
Time complexity: O(2*n)
Space complexity: O(n)
"""


def count_weight(text):
    stack = []
    map_char = {'C': 12, 'H': 1, 'O': 16}
    for i in range(len(text)):
        if text[i] == ')':
            pre_char = stack.pop()
            tmp_value = 0
            while pre_char != '(':
                tmp_value += int(pre_char)
                pre_char = stack.pop()
            stack.append(tmp_value)
        elif text[i].isdigit():
            stack.append(stack.pop() * int(text[i]))
        elif text[i] == '(':
            stack.append(text[i])
        else:
            stack.append(map_char[text[i]])
    return sum(stack)


if __name__ == '__main__':
    text = input()
    print(count_weight(text))
    # print(count_weight("COOH"))
    # print(count_weight("CH(CO2H)3"))
    # print(count_weight("((CH)2(OH2H)(C(H))O)3"))
