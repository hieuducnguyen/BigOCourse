"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    T = int(input())
    input()
    for i in range(T):
        name_dict = {}
        count = 0
        while True:
            try:
                name = input()
                if name == "":
                    break
            except EOFError as e:
                break
            name_dict[name] = name_dict.get(name, 0) + 1
            count += 1
        sorted_name = sorted(name_dict.keys())
        for name in sorted_name:
            print("{} {:.4f}".format(name, name_dict[name] * 100 / count))
        if i != T - 1:
            print()
