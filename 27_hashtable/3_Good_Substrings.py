"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 15/01/2022
"""
if __name__ == '__main__':
    strg = input()
    good_char_list = list(map(int, list(input())))
    K = int(input())
    good_char = set()
    for i in range(26):
        if good_char_list[i] == 1:
            good_char.add(i)
    fre_arr = [0] * (len(strg) + 1)
    len_str = len(strg)
    result = set()
    for i in range(1, len_str + 1):
        if good_char.__contains__(ord(strg[i - 1]) - ord("a")):
            fre_arr[i] = fre_arr[i - 1] + 1
        else:
            fre_arr[i] = fre_arr[i - 1]
    for i in range(len_str):
        for k in range(i + 1, len_str + 1):
            if (k - i) - (fre_arr[k] - fre_arr[i]) <= K:
                result.add(strg[i: k])
            else:
                break
    #print(result)
    print(len(result))
