"""
Link: https://www.spoj.com/problems/OPCPIZZA/
Time complexity: O(T * N)
Space complexity: O(T * N)
Author: Nguyen Duc Hieu
"""

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        input_list = list(map(int, input().split()))
        map_sum = {}
        counter = 0
        for u in range(N):
            if input_list[u] in map_sum:
                map_sum[input_list[u]] = (u, map_sum.get(input_list[u])[1] + 1)
            else:
                map_sum[input_list[u]] = (u, 1)
        for u in range(N):
            if input_list[u] not in map_sum:
                continue
            if M - input_list[u] == input_list[u] and map_sum.get(input_list[u])[1] <= 1:
                continue
            if (M - input_list[u]) in map_sum:
                counter += 1
                if map_sum.get(M - input_list[u])[1] == 1:
                    map_sum.pop(M - input_list[u])
                else:
                    map_sum[M - input_list[u]] = (M - input_list[u], map_sum.get(M - input_list[u])[1] - 1)
                if map_sum.get(input_list[u])[1] == 1:
                    map_sum.pop(input_list[u])
                else:
                    map_sum[input_list[u]] = (input_list[u], map_sum.get(input_list[u])[1] - 1)
        print(counter)
