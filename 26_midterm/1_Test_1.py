if __name__ == '__main__':
    N = int(input())
    for n in range(N):
        number_string = input()
        sum_val = 0
        char_list = []
        for i in number_string:
            sum_val += int(i)
            char_list.append(chr(int(i) + ord('a')))
        string_val = "".join(char_list)
        check_str = ""
        for i in range(sum_val // len(string_val) + 1):
            check_str += string_val
        check_str = check_str[:sum_val]
        start = 0
        end = len(check_str) - 1
        while start <= end:
            if check_str[start] == check_str[end]:
                start += 1
                end -= 1
            else:
                print("NO")
                break
        else:
            print("YES")
