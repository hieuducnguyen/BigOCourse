"""
Link: https://codeforces.com/problemset/problem/520/A
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    N = int(input())
    checker = [False for _ in range(26)]
    text = input()
    for character in text:
        checker[ord(character.lower()) - ord('a')] = True
    result = "YES" if sum(checker) == 26 else "NO"
    print(result)
