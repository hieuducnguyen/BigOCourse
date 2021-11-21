"""
Source: BigO
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    text = input()
    count = 1
    for i in text:
        if i.isupper():
            count += 1
    print(count)
