"""
Link: https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1498
Time complexity: O(T * (E * V)) = O (T * N * N)
Space complexity: O(T * N)
Author: Nguyen Duc Hieu
"""

NEG_INF = -int(1e10)


def bellman_ford(source, edge_list, N):
    dist = [NEG_INF] * N
    dist[source] = 100
    for i in range(N - 1):
        change = False
        for u, v, w in edge_list:
            if dist[u] > 0 and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                change = True
        if not change:
            break
    for i in range(N):
        change = False
        for u, v, w in edge_list:
            if dist[u] > 0 and dist[u] + w > dist[v]:
                dist[v] = -NEG_INF
                change = True
        if not change:
            break
    return dist


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == -1:
            break
        energy_list = [0] * N
        edge_list = []
        for i in range(N):
            out_room = list(map(int, input().split()))
            energy = out_room.pop(0)
            energy_list[i] = energy
            out_edge = out_room.pop(0)
            for room in out_room:
                edge_list.append((i, room - 1, 0))
        for i in range(len(edge_list)):
            u, v, w = edge_list[i]
            edge_list[i] = (u, v, energy_list[v])
        dist = bellman_ford(0, edge_list, N)
        if dist[N - 1] >= 0:
            print("winnable")
        else:
            print("hopeless")
