"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 04/01/2022
"""


class Person:
    def __init__(self, index, action):
        self.index = index
        self.action = action

    def __str__(self):
        return "Person(index={} ; action={}".format(self.index, self.action)


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        input_list = list(map(int, input().split()))
        sell = []
        buy = []
        for i in range(N):
            if input_list[i] == 0:
                continue
            if input_list[i] > 0:
                buy.append(Person(i, input_list[i]))
            else:
                sell.append(Person(i, input_list[i]))
        work = 0
        while len(buy) > 0:
            work += abs(buy[-1].index - sell[-1].index) * min(abs(buy[-1].action), abs(sell[-1].action))
            if abs(buy[-1].action) > abs(sell[-1].action):
                buy[-1].action += sell[-1].action
                sell.pop()
            elif abs(buy[-1].action) < abs(sell[-1].action):
                sell[-1].action += buy[-1].action
                buy.pop()
            else:
                buy.pop()
                sell.pop()
        print(work)
