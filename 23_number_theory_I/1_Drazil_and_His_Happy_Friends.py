"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 06/01/2022
"""
if __name__ == '__main__':
    N, M = map(int, input().split())
    num_boy, *boys = map(int, input().split())
    num_girl, *girls = map(int, input().split())
    happy_boy = [False] * N
    happy_girl = [False] * M
    for i in boys:
        happy_boy[i] = True
    for i in girls:
        happy_girl[i] = True
    for i in range(N * M):
        if happy_boy[i % N] or happy_girl[i % M]:
            happy_boy[i % N] = True
            happy_girl[i % M] = True
    print("Yes" if sum(happy_boy) == N and sum(happy_girl) == M else "No")
