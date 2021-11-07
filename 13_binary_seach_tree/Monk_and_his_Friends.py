"""
Link:
Time complexity: O(N)
Space complexity: O(N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        student_set = set()
        student_list = list(map(int, input().split()))
        for k in range(N):
            student_set.add(student_list[k])
        for k in range(N, N + M):
            if student_list[k] in student_set:
                print("YES")
            else:
                print("NO")
            student_set.add(student_list[k])
