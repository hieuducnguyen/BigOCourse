"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 02/01/2022
"""


def count_val(line):
    val = 0
    for sign in line:
        if sign == "+":
            val += 1
        else:
            val -= 1
    return val


def process_undefind(line, tmp_line, end, count, result, total_case):
    if len(tmp_line) == end:
        if count_val(tmp_line) == count:
            result.append(tmp_line)
        total_case.append(tmp_line)
        return
    if line[len(tmp_line)] == "?":
        for sign in ["+", "-"]:
            process_undefind(line, tmp_line + sign, end, count, result, total_case)
    else:
        process_undefind(line, tmp_line + line[len(tmp_line)], end, count, result, total_case)


if __name__ == '__main__':
    first_line = input()
    first_count = count_val(first_line)
    second_line = input()
    total_case = []
    result = []
    process_undefind(second_line, "", len(second_line), first_count, result, total_case)
    print("{:.11f}".format(len(result) / len(total_case)))
