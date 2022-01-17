"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 02/01/2022
"""
from collections import Counter

direct_x = [-1, -1, -1, 0, 0, 1, 1, 1]
direct_y = [1, 0, -1, 1, -1, 1, 0, -1]
VOWEL = ["U", "E", "O", "A", "I", "Y"]


def find_word(start_x, start_y, len, tmp_result, result, matrix_list):
    if len == 0:
        for i in range(2):
            tmp = ""
            for x, y in tmp_result:
                tmp += matrix_list[i][x][y]
            counter = Counter(list(tmp))
            num_vowel = 0
            for v in VOWEL:
                num_vowel += counter[v]
            if num_vowel == 2:
                result[i].append(tmp)
        return
    for i in range(8):
        new_x = start_x + direct_x[i]
        new_y = start_y + direct_y[i]
        if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (new_x, new_y) not in tmp_result:
            tmp_result.append((new_x, new_y))
            find_word(new_x, new_y, len - 1, tmp_result, result, matrix_list)
            tmp_result.pop()


if __name__ == '__main__':
    first = True
    while True:
        text = input()
        if text == "#":
            break
        if not first:
            print()
        first = False
        matrix_list = [[], []]
        for _ in range(4):
            text_list = text.split("    ")
            for i in range(2):
                matrix_list[i].append(text_list[i].split(" "))
            text = input()  # last iteration read blank row
        result = [[], []]
        for i in range(4):
            for j in range(4):
                tmp_result = [(i, j)]
                find_word(i, j, 3, tmp_result, result, matrix_list)
        have_common = False
        result_words = sorted(list(set(result[0])))
        for word in result_words:
            if word in result[1]:
                print(word)
                have_common = True
        if not have_common:
            print("There are no common words for this pair of boggle boards.")
