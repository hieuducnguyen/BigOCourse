"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 18/01/2022
"""
INF = int(1e9)
if __name__ == '__main__':
    map_ = dict()
    for i in range(INF // 4):
        map_[i] = i
    print(len(map_))
