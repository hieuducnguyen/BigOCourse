"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 05/01/2022
"""
import copy


class Event:
    def __init__(self, id, isFirst):
        self.id = id
        self.isFirst = isFirst

    def __str__(self):
        return "Event(id={} ; isFirst={}".format(self.id, self.isFirst)


if __name__ == '__main__':
    N = int(input())
    time_list = list(map(int, input().split()))
    event_list = [Event(0, False), Event(0, True)]
    num_event = 1
    for i in range(2, N + 1):
        if event_list[time_list[i - 1]].isFirst:
            new_event = copy.deepcopy(event_list[time_list[i - 1]])
            event_list.append(new_event)
            event_list[time_list[i - 1]].isFirst = False
        else:
            event_list.append(Event(num_event, True))
            num_event += 1
    # print(*event_list, sep=" ||| ")
    print(num_event)
