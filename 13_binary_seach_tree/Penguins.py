"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    N = int(input())
    frequence = {}
    max_count = 0
    name_max_count = ""
    for i in range(N):
        name = input()
        frequence[name] = frequence.get(name, 0) + 1
        if frequence[name] > max_count:
            name_max_count = name
            max_count = frequence[name]
    print(name_max_count)
