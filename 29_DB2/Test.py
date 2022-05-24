"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 23/01/2022
"""
import random

if __name__ == '__main__':
    result = set()
    for i in range(2 ** 63):
        tmp = []
        for j in range(60):
            tmp.append(chr(random.randint(0, 25) + ord("a")))
        result.add("".join(tmp))
        if i % 1000 == 0:
            print(len(result))
    print(*result, sep="")
