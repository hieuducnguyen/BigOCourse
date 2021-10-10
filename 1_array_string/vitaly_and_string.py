"""
Link: https://codeforces.com/contest/518/problem/A
Time complexity: O(n)
Space complexity: O(1)
"""


def gen_next_string():
    first_text = input()
    second_text = input()
    result = ''
    carry = 1
    for i in range(len(first_text) - 1, -1, -1):
        if carry:
            if first_text[i] == 'z':
                result = 'a' + result
            else:
                result = chr(ord(first_text[i]) + 1) + result
                carry = 0
        else:
            result = first_text[:i + 1] + result
            break
    if result >= second_text:
        return 'No such string'
    else:
        return result


if __name__ == '__main__':
    print(gen_next_string())
