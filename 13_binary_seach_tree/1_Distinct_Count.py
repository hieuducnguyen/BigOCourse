"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, X = map(int, input().split())
        input_list = list(map(int, input().split()))
        input_set = set(input_list)
        if len(input_set) == X:
            print("Good")
        elif len(input_set) < X:
            print("Bad")
        else:
            print("Average")
