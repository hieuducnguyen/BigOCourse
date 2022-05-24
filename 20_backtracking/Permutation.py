"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 28/12/2021
"""
import copy


def permutaion(s, start, end):
    if start == end:
        print(s)
        return
    for i in range(start, end):
        s[start], s[i] = s[i], s[start]
        permutaion(s, start + 1, end)
        s[start], s[i] = s[i], s[start]


def permutaion2(s, start, end, result):
    if start == end:
        result.append(copy.deepcopy(s))
        return
    for i in range(start, end):
        dup = False
        for k in range(start, i):
            if s[k] == s[i]:
                dup = True
        if not dup:
            s[start], s[i] = s[i], s[start]
            permutaion2(s, start + 1, end, result)
            s[start], s[i] = s[i], s[start]

# def permutaion3(s, start, end, result):
#     if start == end:



if __name__ == '__main__':
    s = list("AABB")
    results = []
    permutaion2(s, 0, len(s), results)
    for result in results:
        print(*result, sep=" ")
    print("result")
    print(results)
    print(len(results))
