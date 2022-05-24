"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 18/01/2022
"""
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        str = input()
        patt = input()
        patt_set = set(list(patt))
        for i in range(len(str)):
            if str[i] in patt_set:
                print(str[i])
                break
        else:
            print("No character present")
