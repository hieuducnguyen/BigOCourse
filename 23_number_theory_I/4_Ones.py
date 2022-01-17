"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 06/01/2022
"""
if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            result = 1
            count = 1
            while True:
                if result % N == 0:
                    print(count)
                    break
                result = result * 10 + 1
                count += 1
        except EOFError:
            break
