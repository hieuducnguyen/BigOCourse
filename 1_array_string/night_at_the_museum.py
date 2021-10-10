'''
Link: https://codeforces.com/contest/731/problem/A
Time complexity: O(n)
Space complexity: O(1)
'''
def smallest_rotate():
    name = input()
    start = ord('a')
    result = 0
    for value in map(ord, name):
        diff = abs(value - start)
        result += min(diff, 26 - diff)
        start = value
    return result


if __name__ == '__main__':
    print(smallest_rotate())
