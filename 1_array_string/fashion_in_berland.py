'''
Link: https://codeforces.com/problemset/problem/691/A
Time complexity: O(n)
Space complexity: O(n)
'''

def check_fashion_berland():
    num_button = int(input())
    if num_button == 1:
        return int(input()) == 1
    fasten_button = list(map(int, input().split()))
    return sum(fasten_button) == num_button - 1


if __name__ == '__main__':
    if check_fashion_berland():
        print("YES")
    else:
        print("NO")

