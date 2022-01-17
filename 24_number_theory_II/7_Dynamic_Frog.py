"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 13/01/2022
"""
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, D = map(int, input().split())
        list_input = input().split()
        last_point = 0
        max_distance = 0
        for val in list_input:
            if val.split("-")[0] == "B":
                new_point = int(val.split("-")[1])
                max_distance = max(max_distance, new_point - last_point)
                last_point = new_point
        max_distance = max(max_distance, D - last_point)
        print("Case {}: {}".format(t + 1, max_distance))
