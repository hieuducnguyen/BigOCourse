"""
Link: 
Time complexity: O(N)
Space complexity: O(N)
Created by Hieu Nguyen on 15/01/2022
"""
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        start_time = list(map(int, input().split()))
        end_time = list(map(int, input().split()))
        event_list = []
        for i in range(N):
            event_list.append((end_time[i], start_time[i], i + 1))
        event_list.sort()
        TS = 0
        i = 0
        num_event = list()
        while i < N:
            if event_list[i][1] > TS:
                TS = event_list[i][0]
                num_event.append(event_list[i][2])
            i += 1
        print(*num_event)
